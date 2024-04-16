#this script finds the number of each TE family found in the genome

fout = open('wy-counts.txt','w')
families = {}
for line in open('wy-families.txt'):
	l = line.strip()
	if l in families.keys():
		families[l] += 1
	else:
		families[l] = 1

for family,count in families.items():
	fout.write(f'{family} \t {count}\n')

fout.close()

