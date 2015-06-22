datafile = file('coordiante nations.txt') 
file_out=open("file_final.txt","w")
for line in datafile:
	ind=0
	string=list()
	ris=""
	for i in range(0,len(line)):
		if(ind==0 and line[i].isdigit()):
			string.append('"'+line[0:i-1]+'",')
			ind=1
			j=i
		elif(ind==1 and line[i]==" "):
			string.append(line[j:i]+'.')
			ind=2
			t=i
		elif(ind==2 and line[i]==" "):
			string.append(line[t+1:i])
			ind=3
		elif(ind==3 and line[i]==","):
			if(line[i-1]=="S"):
				string[1]="-"+string[1]
			string.append(",")
			ind=4
			j=i
		elif(ind==4 and line[i]==" "):
			string.append(line[j+1:i]+'.')
			ind=5
			t=i
		elif(ind==5 and line[i]==" "):
			string.append(line[t+1:i])
			ind=6
		elif(ind==6 and line[i]=="W"):
			string[4]="-"+string[4]
			ind=7
	for x in range(0,len(string)):
		ris=ris+string[x]
	file_out.write(ris+"\n")

