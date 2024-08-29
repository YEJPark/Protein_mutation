import pandas as pd

# Read the Excel file
file_path = './result/modified_sequences.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Initialize a list to store the commands
commands = []

# Iterate over each row and generate the elaspic2 command
for index, row in df.iterrows():
    pdb = row['pdb'].replace('.pdb', '')  # Extract PDB code
    protein_sequence = row['protein_sequence']
    ligand_sequence = row['ligand_sequence'] if 'ligand_sequence' in row and pd.notna(row['ligand_sequence']) else None
    mutations = row['Predictions']

    # Construct the elaspic2 command
    command = f"python -m elaspic2 --protein-structure ./data/PDB/{pdb}.pdb --protein-sequence {protein_sequence}"
    if ligand_sequence:
        command += f" --ligand-sequence {ligand_sequence}"
    command += f" --mutations {mutations} > elaspic_result/{index}"

    # Append the command to the list
    commands.append(command)

# Convert the list to a DataFrame
commands_df = pd.DataFrame(commands, columns=['Command'])

# Save the DataFrame to a TSV file
commands_df.to_csv('elaspic2_commands.tsv', sep='\t', index=False)
