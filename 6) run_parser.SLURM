#!/bin/bash
#SBATCH --job-name=paper_parser
#SBATCH --output=parser_%j.out
#SBATCH --error=parser_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=100             # 👈 one task per keyword (matches keywords.txt lines)
#SBATCH --time=00:30:00          # ⏳ bumped time since 100 tasks will take longer
#SBATCH --partition=compute
#SBATCH --account=csd946         # 👈 your allocation group

module load python/3.9.0
source ~/semantic-scholar-parser/venv/bin/activate

# Each task grabs a different keyword line from keywords.txt
srun bash -c 'keyword=$(sed -n "$((SLURM_PROCID+1))p" keywords.txt); python parser.py "$keyword"'
