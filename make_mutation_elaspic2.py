import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline
import pandas as pd
from tqdm import tqdm

# Initialization
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model_name = 'Rostlab/prot_bert'
model = AutoModelForMaskedLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)
pip = pipeline('fill-mask', model=model, tokenizer=tokenizer, device=2 if device == "cuda" else -1)

# Read the Excel file
file_path = 'make_mutation_elaspic2.xlsx' 
df = pd.read_excel(file_path)

# Check and add necessary columns
if 'Predictions' not in df.columns:
    df['Predictions'] = None

# Define standard amino acids
#standard_aa = set('ARNDCEQGHILKMFPSTWYV')
standard_aa = set(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])

# Function to predict mutations
def predict_sequence(sequence):
    predictions_str = ""
    
    for i, aa in tqdm(enumerate(sequence), total=len(sequence), desc="Predicting"):
        if aa in standard_aa:
            masked_sequence = list(sequence)
            masked_sequence[i] = '[MASK]'
            masked_input = ' '.join(masked_sequence)
            results = pip(masked_input)

            for res in results:
                if res['token_str'] in standard_aa and res['token_str'] != aa and res['score'] >= 0.5:
                    prediction = f"{aa}{i+1}{res['token_str']}"
                    # Add predictions to the string with periods but no spaces
                    predictions_str += ('.' + prediction) if predictions_str else prediction
    
    return predictions_str


# Process each protein sequence
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing sequences"):
    protein_sequence = row['protein_sequence']  # Adjust this column name if necessary
    prediction_str = predict_sequence(protein_sequence)
    df.at[index, 'Predictions'] = prediction_str

# Save to a new Excel file
new_file_path = 'modified_sequences.xlsx'
df.to_excel(new_file_path, index=False)
