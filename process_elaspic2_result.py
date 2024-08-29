import os
import json
import pandas as pd

# Directory containing the files
directory = 'elaspic2_result'

# Prepare a list to store all the data
all_data = []

# Function to check if a line contains the DomainDef or Sequence information
def is_valid_line(line):
    return "DomainDef(" in line or all(char in "ACDEFGHIKLMNPQRSTVWY" for char in line.strip())

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(''):  # Adjust the extension if needed
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()

            # Check if the file has at least two lines (DomainDef and Sequence)
            if len(lines) < 2:
                continue  # Skip file if it doesn't meet the criteria

            # Extract DomainDef and sequence
            domain_def_line = lines[0].strip()
            sequence_line = lines[1].strip()

            # Check for valid DomainDef and Sequence lines
            if not (is_valid_line(domain_def_line) and is_valid_line(sequence_line)):
                continue  # Skip file if lines are not valid

            # Extract the actual DomainDef and sequence from lines
            domain_def = domain_def_line
            sequence = sequence_line

            # Parse each mutation entry from the third line onwards
            for line in lines[2:]:
                try:
                    mutation_data = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue  # Skip invalid JSON lines

                mutation = mutation_data.get('mutation')
                protbert_core = mutation_data.get('protbert_core')
                proteinsolver_core = mutation_data.get('proteinsolver_core')
                el2core = mutation_data.get('el2core')

                # Check if all necessary data is present
                if not all([mutation, protbert_core, proteinsolver_core, el2core]):
                    continue  # Skip incomplete data lines

                # Append to the list, including the filename
                all_data.append([filename, domain_def, sequence, mutation, protbert_core, proteinsolver_core, el2core])

# Check if we have collected any data
if not all_data:
    print("No valid data was collected from the files.")
else:
    # Create a DataFrame with an additional 'Filename' column
    df = pd.DataFrame(all_data, columns=['Filename', 'DomainDef', 'Sequence', 'Mutation', 'Protbert_core', 'Proteinsolver_core', 'El2core'])

    # Save to Excel
    excel_filename = './result/aggregated_elaspic_data.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f"Data saved to {excel_filename}")
