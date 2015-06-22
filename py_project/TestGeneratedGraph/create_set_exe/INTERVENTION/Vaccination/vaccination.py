def stat(graph,change,t):
	global Matrix
	result=graph.cypher.execute("MATCH n where n.stat='S' return count(n) as ris")
	S=print_single(result)
	print "Number of S: %d" % S
	Matrix[t][0]=S

	result=graph.cypher.execute("MATCH n where n.stat='V' return count(n) as ris")
	V=print_single(result)
	print "Number of V: %d" % V
	Matrix[t][3]=V

	result=graph.cypher.execute("MATCH n where n.stat='I' return count(n) as ris")
	I=print_single(result)
	print "Number of I: %d" % I
	Matrix[t][1]=I

	result=graph.cypher.execute("MATCH n where n.stat='R' return count(n) as ris")
	R=print_single(result)
	print "Number of R: %d" % R
	Matrix[t][2]=R



	print "Number of change: %d" % len(change)
	print ""
	# the vaccine will be apply just if S/I grater then 30%
	if(S>0):
		if((float(I)/float(S)) > 0.1):
			return 1


def crea_matrix_file(day_simu):
	global Matrix
	out_file = open("Matrix.csv","w")
	out_file.write('S,I,R,V \n')
	for i in range(0,day_simu+1):
		out_file.write('%d,%d,%d,%d \n' % (Matrix[i][0],Matrix[i][1],Matrix[i][2],Matrix[i][3]))
	out_file.close()


def apply_vacc(graph,rate_effectivenss,rate_application_vacc):
	result=graph.cypher.execute("MATCH n where n.stat='S' return count(n) as ris")
	S=print_single(result)
	for i in range(0,int(rate_application_vacc*S)):
		rand= random.random()
		if (rand<rate_effectivenss):
			graph.cypher.execute("MATCH n where n.stat='S'set n.stat='V' return n limit 1")

def decision_vac(N_vac,N_non):
	if (float(N_vac+N_non)!=0):
		lamnda=(float(N_non)/float(N_vac+N_non))
		r=0.7
		if(r>lamnda):
			print lamnda
			return 1
		else:
			return 0


from py2neo import Graph
import random
import json
from function import * 

change= list()
arr=list()
vaccination=list()
rate_effectivenss=0.7 # this rate indicate how is effective the vaccine
rate_application_vacc=0.05 # this means the rate of the "S" people will be vaccinated 
day_simu=20;
Matrix = [[0 for y in xrange(4)] for x in xrange(day_simu+1)]
graph = Graph()
result=graph.cypher.execute("MATCH (n) return count(n) as ris")
nodes=print_single(result)
print "Number of nodes: %d" % nodes

vacc=stat(graph,"",0)
create_map(graph)

cond=1 #trick, this permit to the code to enter just ones to vacc=cond in order to apply the interventions just ones
for t in range(0,day_simu):
	if(vacc==cond):
		apply_vacc(graph,rate_effectivenss,rate_application_vacc)
		cond=2

	del change[:]
	del vaccination[:]
	for i in range(0,nodes):
		query= "MATCH (n {name : %d })-[r]-(x) where n.stat='S' and x.stat='I' return r as ris" % i
		result=graph.cypher.execute(query)
		del arr[:]
		for r in result:
			arr.append(r.ris["duration"])
		if arr:
			prob= calculate_prob(arr)
			rand= random.random()
			if (rand < prob):
				change.append(i)
		if(cond==2):
			query= "MATCH (n {name : %d })-[r]-(x) where n.stat='S' return x as ris" % i
			result=graph.cypher.execute(query)
			N_vac=0
			N_non=0
			for r in result:
				if(r.ris['stat']=="V"):
					N_vac=N_vac+1
				elif(r.ris['stat']=="S"):
					N_non=N_non+1
			ris= decision_vac(N_vac,N_non)
			if (ris==1):
				vaccination.append(i)

	hive_plot_entire_graph(t,graph)			
	update_label(graph,change,vaccination,t)
	apply_change(change,vaccination,graph)
	vacc=stat(graph,change,t+1)
	


crea_matrix_file(day_simu)

