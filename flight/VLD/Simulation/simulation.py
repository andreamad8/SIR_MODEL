def stat(graph,change,t):
	global Matrix
	result=graph.cypher.execute("MATCH n where n.stat='S' return count(n) as ris")
	out=print_single(result)
	print "Number of S: %d" % out
	Matrix[t][0]=out
	result=graph.cypher.execute("MATCH n where n.stat='I' return count(n) as ris")
	out=print_single(result)
	print "Number of I: %d" % out
	Matrix[t][1]=out
	result=graph.cypher.execute("MATCH n where n.stat='R' return count(n) as ris")
	out=print_single(result)
	print "Number of R: %d" % out
	Matrix[t][2]=out
	print "Number of change: %d" % len(change)
	print ""

def crea_matrix_file(day_simu):
	global Matrix
	out_file = open("Matrix.csv","w")
	out_file.write('S,I,R \n')
	for i in range(0,day_simu+1):
		out_file.write('%d,%d,%d \n' % (Matrix[i][0],Matrix[i][1],Matrix[i][2]))
	out_file.close()

def plot_color_file(change_Json,country_iso,S,I,R):
		global ind	
		if(I==0):
			color="#FFCC00"
		else:
			if (float(I)/float(S))>0 and (float(I)/float(S))<1 and (float(R)/float(S))<20:
				color="#FFA500"
			elif (float(I)/float(S))>=1 and (float(R)/float(S))<30:
				color="#FF4900"
			elif (float(R)/float(S))>30:
				color="#008000"
			else:
				color="#008000"

		if(ind==0):
			change_Json.write('"%s":"%s"' % (country_iso,color))
			ind=1
		else:
			change_Json.write(',"%s":"%s"' % (country_iso,color))


def SIR_COUNTRY(graph,i,change_Json):
	b=0.5
	l=0.112
	query= "MATCH (n) where id(n)=%d return n as ris" % i
	result=graph.cypher.execute(query)
	for r in result:
		old_S=r.ris["S"]
		old_I=r.ris["I"]
		old_R=r.ris["R"]
		country_iso=r.ris["iso"]
		stat=r.ris["stat"]
	P=old_S+old_I+old_R
	S=old_S-int(((b*old_I)/P)*old_S)
	I=old_I+int(((b*old_I)/P)*old_S)-int(l*old_I)
	R=old_R+int(l*old_I) 
	query= "MATCH (n) where id(n)=%d set n.S=%d set n.I=%d set n.R=%d" % (i,S,I,R)
	result=graph.cypher.execute(query)
	plot_color_file(change_Json,country_iso,S,I,R)


from py2neo import Graph
import random
import json
from function import * 

change_Json = open("change.json","w")


change=list()
arr=list()
day_simu=200;
Matrix = [[0 for y in xrange(3)] for x in xrange(day_simu+1)]
graph = Graph()
result=graph.cypher.execute("MATCH (n) return count(n) as ris")
nodes=print_single(result)
print "Number of nodes: %d" % nodes

stat(graph,"",0)
change_Json.write('[')
global ind
for t in range(0,day_simu):
	del change[:]
	change_Json.write('\n{')
	ind=0
	for i in range(0,nodes):
		SIR_COUNTRY(graph,i,change_Json)
		query= "MATCH (n)<-[r]-(x) where id(n)=%d and n.stat='S' and x.stat='I' and x.I/x.S>=1 return r as ris" % i
		result=graph.cypher.execute(query)
		del arr[:]
		for r in result:
			arr.append(r.ris["num_pass_norm"])
		if arr:
			r=0.8
			dur=calculate_prob(arr)	
			prob= (1-pow((1-r),dur))	
			rand= random.random()
			if (rand <= prob):
				change.append([i,dur])		
	apply_change(change,graph,change_Json)
	stat(graph,change,t+1)
	change_Json.write('},')
	

change_Json.write(']')
change_Json.close()
crea_matrix_file(day_simu)

