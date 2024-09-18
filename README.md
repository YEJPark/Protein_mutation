# Mutation Analysis Workflow

This repository provides a step-by-step guide to performing mutation analysis based on protein sequences and structures.

## Workflow Overview

Follow the steps below to run the mutation analysis using the provided scripts.

### 1. Prepare `protein_sequence.xlsx`

- Search for the target protein sequence (e.g., CD2) on [UniProt](https://www.uniprot.org/).
- Find the corresponding structure data (PDB entry) on the [Protein Data Bank (PDB)](https://www.rcsb.org/).
- Save the relevant information in `protein_sequence.xlsx`.

### 2. Generate Mutated Sequences

- Run one of the following scripts to generate the mutated protein sequences:
  - `make_mutation.py`
  - `make_mutation_with_score.py`
  
### 3. Create ELASPIC2 Commands

- Ensure the `elaspic2_result` folder is created in the project directory.
- Run `make_command.py` to generate the necessary commands for ELASPIC2.
- Save the output commands in a bash script file (e.g., `elaspic2_commands.sh`).

### 4. Execute the Bash Script

- Run the bash script to initiate the ELASPIC2 analysis:
  ```bash
  sh elaspic2_commands.sh
