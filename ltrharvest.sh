#!/bin/bash
#SBATCH --time=96:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=32gb
#SBATCH --partition=Orion

module use ~/sw/modules
module load genome-tools

gt suffixerator -db ae-aegypti.fa -indexname ae-aegypti.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index ae-aegypti.fa -v -out pred-aaeg.fsa -outinner pred-inner-aaeg.fsa -gff3 pred-aaeg.gff3

gt suffixerator -db ae-albopictus.fa -indexname ae-albopictus.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index ae-albopictus.fa -v -out pred-aalb.fsa -outinner pred-inner-aalb.fsa -gff3 pred-aalb.gff3

gt suffixerator -db an-coluzzii.fa -indexname an-coluzzii.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index an-coluzzii.fa -v -out pred-acol.fsa -outinner pred-inner-acol.fsa -gff3 pred-acol.gff3

gt suffixerator -db an-gambiae.fa -indexname an-gambiae.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index an-gambiae.fa -v -out pred-agam.fsa -outinner pred-inner-agam.fsa -gff3 pred-agam.gff3

gt suffixerator -db cu-qu.fa -indexname cu-qu.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index cu-qu.fa -v -out pred-cqui.fsa -outinner pred-inner-cqui.fsa -gff3 pred-cqui.gff3

gt suffixerator -db cu-tarsalis.fa -indexname cu-tarsalis.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index cu-tarsalis.fa -v -out pred-ctar.fsa -outinner pred-inner-ctar.fsa -gff3 pred-ctar.gff3

gt suffixerator -db wy-smithii.fa -indexname wy-smithii.fa -tis -suf -lcp -des -ssp -sds -dna
gt ltrharvest -index wy-smithii.fa -v -out pred-wsmi.fsa -outinner pred-inner-wsmi.fsa -gff3 pred-wsmi.gff3

