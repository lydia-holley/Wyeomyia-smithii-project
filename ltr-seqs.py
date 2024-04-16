fout = open("aaeg-ltr.fasta","w")
headers = []
count = 0
keep = False
with open("aaeg.fasta.out","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]
			if sequence in headers:
				count += 1
				if count == 4 or count == 5:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				headers.append(sequence)
				count = 1
		else:
			if keep == True:
				fout.write(line)
			else:
				continue
fout.close()

fout = open("aalb-ltr.fasta","w")
headers = []
count = 0
keep = False
with open("aalb.fasta.out","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]
			if sequence in headers:
				count += 1
				if count == 4 or count == 5:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				headers.append(sequence)
				count = 1
		else:
			if keep == True:
				fout.write(line)
			else:
				continue
fout.close()

fout = open("acol-ltr.fasta","w")
headers = []
count = 0
keep = False
with open("acol.fasta.out","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]
			if sequence in headers:
				count += 1
				if count == 4 or count == 5:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				headers.append(sequence)
				count = 1
		else:
			if keep == True:
				fout.write(line)
			else:
				continue
fout.close()

fout = open("ctar-ltr.fasta","w")
headers = []
count = 0
keep = False
with open("ctar.fasta.out","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]
			if sequence in headers:
				count += 1
				if count == 4 or count == 5:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				headers.append(sequence)
				count = 1
		else:
			if keep == True:
				fout.write(line)
			else:
				continue
fout.close()

fout = open("wsmi-ltr.fasta","w")

headers = []
count = 0
keep = False

with open("wsmi.fasta.out","r") as fh:

	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]

			if sequence in headers:
				count += 1

				if count == 4 or count == 5:
					keep = True
					fout.write(line)

				else:
					keep = False

			else:

				headers.append(sequence)
				count = 1

		else:
			if keep == True:
				fout.write(line)

			else:
				continue

fout.close()

fout = open("cqui-ltr.fasta","w")

headers = []
count = 0
keep = False

with open("cqui.fasta.out","r") as fh:

	for line in fh:
		if line.startswith(">"):
			sequence = line.split(":")[0]

			if sequence in headers:
				count += 1

				if count == 4 or count == 5:
					keep = True
					fout.write(line)

				else:
					keep = False

			else:

				headers.append(sequence)
				count = 1

		else:
			if keep == True:
				fout.write(line)

			else:
				continue
print(headers)
fout.close()
