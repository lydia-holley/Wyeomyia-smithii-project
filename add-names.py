#this script adds species names to fasta headers

#add species namaes to Aedes aegypti file
fout1 = open("./named-families/Aaeg-named.fa","w")

for line in open("./TE-Families/ae-aegypti-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Aaeg_" + oldline
		fout1.write(newline)

	else:
		fout1.write(line)

fout1.close()

#add species names to Aedes albopictus file
fout2 = open("./named-families/Aalb-named.fa","w")

for line in open("./TE-Families/ae-albopictus-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Aalb_" + oldline
		fout2.write(newline)

	else:
		fout2.write(line)

fout2.close()

#add species names to Anopheles coluzzii file
fout3 = open("./named-families/Acol-named.fa","w")

for line in open("./TE-Families/an-coluzzii-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Acol_" + oldline
		fout3.write(newline)

	else:
		fout3.write(line)

fout3.close()

#add species names to Anopheles gambiae file
fout4 = open("./named-families/Agam-named.fa","w")

for line in open("./TE-Families/an-gambiae-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Agam_" + oldline
		fout4.write(newline)

	else:
		fout4.write(line)

fout4.close()

#add species names to Culex quinquefasciatus file
fout5 = open("./named-families/Cqui-named.fa","w")

for line in open("./TE-Families/cu-qu-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Cqui_" + oldline
		fout5.write(newline)

	else:
		fout5.write(line)

fout5.close()

#add species names to Culex tarsalis file
fout6 = open("./named-families/Ctar-named.fa","w")

for line in open("./TE-Families/cu-tarsalis-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Ctar_" + oldline
		fout6.write(newline)

	else:
		fout6.write(line)

fout6.close()

#add species names to Wyeomyia smithii file
fout7 = open("./named-families/Wsmi-named.fa","w")

for line in open("./TE-Families/wyeomyia-families.fa"):
	if line.startswith('>'):
		oldline = line.split('>')[1]
		newline = ">Wsmi_" + oldline
		fout7.write(newline)

	else:
		fout7.write(line)

fout7.close()

