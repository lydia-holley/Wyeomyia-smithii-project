names = []

with open("wsmi-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)


keep = False

for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")

	with open("wsmi-ltr.fasta","r") as file:

		for line in file:

			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)

				else:
					keep = False

			else:
				if keep == True:
					fout.write(line)

				else:
					continue

	fout.close()

names = []
with open("aaeg-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)
keep = False
for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")
	with open("aaeg-ltr.fasta","r") as file:
		for line in file:
			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				if keep == True:
					fout.write(line)
				else:
					continue
	fout.close()

names = []
with open("aalb-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)
keep = False
for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")
	with open("aalb-ltr.fasta","r") as file:
		for line in file:
			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				if keep == True:
					fout.write(line)
				else:
					continue
	fout.close()

names = []
with open("acol-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)
keep = False
for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")
	with open("acol-ltr.fasta","r") as file:
		for line in file:
			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				if keep == True:
					fout.write(line)
				else:
					continue
	fout.close()

names = []
with open("ctar-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)
keep = False
for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")
	with open("ctar-ltr.fasta","r") as file:
		for line in file:
			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)
				else:
					keep = False
			else:
				if keep == True:
					fout.write(line)
				else:
					continue
	fout.close()

names = []

with open("cqui-ltr.fasta","r") as fh:
	for line in fh:
		if line.startswith(">"):
			sequence = line.split("#")[0].lstrip(">")
			if sequence not in names:
				names.append(sequence)


keep = False

for name in names:
	file_name = name + ".fa"
	fout = open(file_name,"w")

	with open("cqui-ltr.fasta","r") as file:

		for line in file:

			if line.startswith(">"):
				if name in line:
					keep = True
					fout.write(line)

				else:
					keep = False

			else:
				if keep == True:
					fout.write(line)

				else:
					continue

	fout.close()
