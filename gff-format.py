fout = open("fixed-pred-aaeg.gff3","w")
with open("pred-aaeg.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)
		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("ae-aegypti.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]
			full_line = sequence + info
			fout.write(full_line)
fout.close()

fout = open("fixed-pred-aalb.gff3","w")
with open("pred-aalb.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)
		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("ae-albopictus.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]
			full_line = sequence + info
			fout.write(full_line)
fout.close()

fout = open("fixed-pred-acol.gff3","w")
with open("pred-acol.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)
		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("an-coluzzii.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]
			full_line = sequence + info
			fout.write(full_line)
fout.close()

fout = open("fixed-pred-ctar.gff3","w")
with open("pred-ctar.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)
		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("cu-tarsalis.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]
			full_line = sequence + info
			fout.write(full_line)
fout.close()

fout = open("fixed-pred-wsmi.gff3","w")

with open("pred-wsmi.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)

		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("wy-smithii.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]

			full_line = sequence + info
			fout.write(full_line)

fout.close()

fout = open("fixed-pred-cqui.gff3","w")

with open("pred-cqui.gff3","r") as fh:
	for line in fh:
		if line.startswith('#'):
			fout.write(line)

		elif line.startswith('seq'):
			seq_num = line.split('q')[1].split('\t')[0]
			intro = "seq" + seq_num
			info = line.split(intro)[1]
			
			with open("cu-qu.fa","r") as file:
				count = -1
				sequence = "pass"
				for l in file:
					if l.startswith(">"):
						count += 1
						if int(seq_num) == int(count):
							l = l.lstrip(">")
							sequence = l.split(" ")[0]

			full_line = sequence + info
			fout.write(full_line)

fout.close()
