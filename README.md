Workflow for Mutation Analysis
This repository outlines the steps to perform mutation analysis based on protein sequences and structures.

Steps:
#1. Create protein_sequence.xlsx:
- Search for the target protein (e.g., CD2) sequence data on UniProt.
- Search for the corresponding PDB entry (structure data) on PDB.

2. Run make_mutation.py or make_mutation_score.py:
- These scripts will generate the mutated sequences.
  
3. Run make_command.py and Create a Bash Script:
- Ensure that the elaspic2_result folder is created beforehand.
- Run make_command.py to generate the necessary commands for ELASPIC2.
- Save the generated commands into a bash script file with the .sh extension.

4. Execute the Bash Script:
- Run the bash script using sh elaspic2_commands.sh.

5. Run process_elaspic2_result.py:
- This script organizes the output files from the ELASPIC2 analysis.
