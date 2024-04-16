#!/bin/bash
#SBATCH --time=96:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem=32gb
#SBATCH --partition=Orion

module load bedtools2

bedtools getfasta -fi ae-aegypti.fa -bed fixed-pred-aaeg.gff3 -fo aaeg.fasta.out
bedtools getfasta -fi ae-albopictus.fa -bed fixed-pred-aalb.gff3 -fo aalb.fasta.out
bedtools getfasta -fi an-coluzzii.fa -bed fixed-pred-acol.gff3 -fo acol.fasta.out
bedtools getfasta -fi cu-tarsalis.fa -bed fixed-pred-ctar.gff3 -fo ctar.fasta.out
bedtools getfasta -fi cu-qu.fa -bed fixed-pred-cqui.gff3 -fo cqui.fasta.out
bedtools getfasta -fi wy-smithii.fa -bed fixed-pred-wsmi.gff3 -fo wsmi.fasta.out

