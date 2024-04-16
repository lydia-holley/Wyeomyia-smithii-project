#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=8GB
#SBATCH --partition=Orion

./orthofinder -f primary_transcripts/

