# this script extracts the TE families in the file

fout = open('wy-families.txt','w')
for line in open('wyeomyia-families.fa'):
	if line.startswith('>'):
		l1 = line.split('#')[1]
		l2 = l1.split(' ')[0] 
		try:
			l3 = l2.split('/')[1]
			fout.write(l3)
			fout.write('\n')
		except:
			fout.write(l2)
			fout.write('\n')

fout.close()
