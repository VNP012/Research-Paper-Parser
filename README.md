# Research-Paper-Parser
HPC cluster based parser for parsing Semantic Scholar research paper using filters, including keywords, dates etc. 
This project provides a scalable tool for retrieving academic research papers from the Semantic Scholar API, designed to run on both local systems and HPC environments such as SDSC Expanse.

 - It supports:
	•	Prompt mode → interactive queries.
	•	Batch mode → multiple keywords from a text file.
	•	HPC scaling with SLURM → large-scale literature retrieval.

 - Features
	•	Retrieve papers by keyword, year range, and venue.
	•	Save results in CSV format for easy analysis.
	•	Scale to 100+ queries with SLURM job submission.
	•	Built with Python 3, requests, pandas, and tested on SDSC Expanse.

 - Builder Setup Guide (HPC Environment)
# 1. Log in to SDSC Expanse
ssh username@login.expanse.sdsc.edu
# Enter your password
# Enter your TOTP code if enabled

# 2. Create and enter the project directory
mkdir semantic-scholar-parser
cd semantic-scholar-parser

# 3. Create the parser script
nano parser.py
# Paste the provided code for parser.py into this file
# Save (Ctrl+O, Enter) and exit (Ctrl+X)

# 4. (Optional) Upload other project files
# keywords.txt, run_parser.slurm, combine_results.py

# 5. Load required modules for Python
# Use `module spider` to check and load the correct Python/Anaconda modules for your HPC system.
# (Examples below are environment-specific and may differ on your cluster.)
module load anaconda3/2021.05

# 6. Create a virtual environment
python -m venv venv
source venv/bin/activate

# 7. Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 8. Test the parser interactively
python parser.py
# Enter a keyword (e.g., nanotechnology) and confirm CSV is created

# 9. (Optional) Batch mode with keywords.txt
nano keywords.txt
# Add multiple keywords, one per line
python parser.py keywords.txt

# 10. (Optional) Run at scale with SLURM
nano run_parser.slurm
# Paste the provided jobscript
sbatch run_parser.slurm
squeue -u username


 - User Workflow (Quick Start)
# Run parser interactively
python parser.py

# Batch mode with keywords.txt
python parser.py keywords.txt

# Download results from Expanse to your local machine
scp "username@login.expanse.sdsc.edu:/home/username/semantic-scholar-parser/results_*.csv" ~/Downloads/

 - Saving Results to Local Machine

From your Mac terminal (not inside Expanse):
scp username@login.expanse.sdsc.edu:/home/username/semantic-scholar-parser/results_nanotechnology.csv ~/Downloads/

Download all results at once:
scp "username@login.expanse.sdsc.edu:/home/username/semantic-scholar-parser/results_*.csv" ~/Downloads/
Files will appear in your Downloads folder.

 - Example Output:
Title,Year,Venue
Photothermal Nanomaterials: A Powerful Light-to-Heat Converter,2023,Chemical Reviews
Green and sustainable synthesis of nanomaterials,2023,Environmental Research
Nanomaterials: An overview of synthesis, classification, and applications,2023,Nano Select
Antibacterial Nanomaterials: Mechanisms and Design Principles,2023,Angewandte Chemie

 - Requirements
Install dependencies in a virtual environment:
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

requirements.txt includes:
requests>=2.25.0
pandas>=1.3.0

 - HPC Notes
	•	This workflow is a reference — commands may require adjustment depending on your cluster configuration, modules, and environment.
	•	Use module spider to discover the correct Python/Anaconda modules.
	•	SLURM enables parallel execution of multiple keyword queries.

 - Repository Contents:
   
parser.py              # Main parser script
keywords.txt           # List of search keywords
run_parser.slurm       # SLURM jobscript for batch runs
combine_results.py     # Utility to merge multiple CSVs
requirements.txt       # Python dependencies
setup.sh               # Quick-start environment setup (optional)
example_output.csv     # Sample CSV output (trimmed)
README.md              # Project documentation
.gitignore             # Exclusions (venv, CSVs, logs)

