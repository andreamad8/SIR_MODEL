datafile = file('file_out.txt') 
file_out=open("file_final.txt","w")
for line in datafile:
	ind=0
	print line[len(line)-1]
	for i in range(0,len(line)):
		if(ind==0 and line[i]=="/"):
			file_out.write(line[0:i]+'",')
			ind=1
		elif(ind==1 and line[i]==','):
			ind=2
		elif(ind==2):
			file_out.write(line[i:len(line)])
			ind=3
	if(ind==0):
		file_out.write(line)