S=10000  	
I=3 
R=0
b=0.5
l=0.112
P=S+I+R
old_S=S
old_I=I
old_R=R
file_out=open("sir.csv",'w')
for t in xrange(1,100):
	S=old_S-int(((b*old_I)/P)*old_S)
	I=old_I+int(((b*old_I)/P)*old_S)-int(l*old_I)
	R=old_R+int(l*old_I) 
	P=S+I+R
	print "number of S: %d" % S
	print "number of I: %d" % I
	print "number of R: %d" % R
	file_out.write("%d,%d,%d \n"%(S,I,R))
	print "%d \n" % P
	old_S=S
	old_I=I
	old_R=R
