#!/bin/bash
#SBATCH --time=96:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=32gb
#SBATCH --partition=Orion

module load clustal-omega

for file in ltr-files/*.fa
do
	clustalo -i $file -o $file-out.stdout
done
