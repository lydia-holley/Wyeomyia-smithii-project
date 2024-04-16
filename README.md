# WyGen Repository:
This repository contains scripts I wrote as a graduate research assistant while working on the Wyeomyia smithii Genome project for Dr. Elizabeth Cooper's Lab at UNC Charlotte. In this project I identified and aged Transposable Elements (TEs) within W.smithii and six other mosquito genome annotations, then I visualized these results.

https://elizcooperlab.com

## Part A:

1. repeatModeler.slurm

Bash script used to identify the TE families in the Wyeomyia smithii genome assembly. Requires genome annotation of Wyeomyia smithii and the repeatmodeler module. I replicated with the 6 other mosquito species genome annotations.

2. add-names.py

Python script to add species name identifiers to each header in the fasta files of TE families identified from repeatmodeler for each of the 7 species. The output from repeatmodeler is required for this script.

3. get-families.py

Python script to extract the TE families that are in each genome. The fasta files with added species identifiers are required for this script. I repeated with the 6 other mosquito species genome annotations.

4. get-family-counts.py

Python script to determine the number of each TE family found within each species. The output from get-families.py is required for this script. I repeated with the 6 other mosquito species.

5. longest_transcripts.sh 

Bash script to get primary transcripts for later input into orthofinder. This script requires proteome files for each investigated species. 

6. OrthoScript.sh

Bash script to run orthofinder on the primary transcripts found in the previous step. The output of interest is Species_Tree/SpeciesTree_rooted.txt

7. iTOL annotation editor

Input SpeciesTree_rooted.txt into iTOL, then use the annotation editor to produce a multi-value bar-chart of TE family counts  

## Part B:

1. ltrharvest.sh

Bash script to run ltrharvst and locate unfragmented LTRs in the mosquito genome annotations. Genome annotations in fasta format are required for this script.

2. gff-format.py 

Python script to alter the format of the ltrharvest output to make it work with getfasta. The ltrharvest output is required for this script.

3. getfasta.sh

Bash script to extract sequences from ltrharvest. The fasta genome annotations and the output from gff-format.py are required for this script.

4. ltr-seqs.py

Python script to extract the long terminal repeats. The getfasta.sh output is required for this script.

5. ltr-files.py

Python script to produce one file for each set of LTR sequences. The ltr-seqs.py output is required for this script.

6. clustal-loop.sh

Bash script to align each of the LTR files we produced from the previous step. The directory containing all of the previous outputs is required for this script.

7. TE_aging.R

R script to determine and visualize the age of the identified LTRs. The aligned outputs from the previous step are required for this script.
