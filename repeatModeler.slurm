#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128gb
#SBATCH --partition=Orion

### Load the RepeatModeler module
module load repeatmodeler

### Set a shortcut to the reference genome
ref=/nobackup/cooper_research/liz/Mosquito/Wyeomyia/new-annotation-2022/wyeomyia.polished.fasta

### Change directories to the folder for the output
cd /nobackup/cooper_research/lydia/Mosquito/Wyeomyia/repeats

### Step 1: Build the Database
BuildDatabase -name wyeomyia -engine ncbi $ref

### Step 2: Run RepeatModeler with the LTR discovery pipeline
RepeatModeler -database wyeomyia -pa 16 -LTRStruct -engine ncbi 2>&1 | tee repeatmodeler.log
