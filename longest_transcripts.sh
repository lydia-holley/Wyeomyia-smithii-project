#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=8GB
#SBATCH --partition=Orion

for f in *fa ; do python /nobackup/cooper_research/lydia/Mosquito/phylo_tree/orthofinder/OrthoFinder/tools/primary_transcript.py $f ; done
