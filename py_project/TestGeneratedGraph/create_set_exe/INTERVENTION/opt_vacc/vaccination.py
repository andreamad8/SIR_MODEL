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
	# the vaccine will be apply just if S/I grater then 10%
	if((float(I)/float(S)) > 0.1):
		print "start vaccination day %d" % t 
		return 1


def crea_matrix_file(day_simu,perc):
	global Matrix
	file_mat="Matrix%d.csv" % perc
	out_file = open(file_mat,"w")
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

from py2neo import Graph
import random
import json
from function import * 
from set_graph import * 

change= list()
arr=list()
rate_effectivenss=0.7 # this rate indicate how is effective the vaccine
day_simu=20;

graph = Graph()




for perc in xrange(1,9):
	reset_label(graph)
	create_I(graph,8)
	
	Matrix = [[0 for y in xrange(4)] for x in xrange(day_simu+1)]
	vacc=stat(graph,"",0)
	result=graph.cypher.execute("MATCH (n) return count(n) as ris")
	nodes=print_single(result)
	print "Number of nodes: %d" % nodes

	cond=1 #trick, this permit to the code to enter just ones to vacc=cond in order to apply the interventions just ones
	for t in range(0,day_simu):
		if(vacc==cond):
			rate_application_vacc=float("0.%d"% perc)
			apply_vacc(graph,rate_effectivenss,rate_application_vacc)
			cond=10

		del change[:]
		for i in range(0,nodes):
			query= "MATCH (n {name : %d })-[r]-(x) where n.stat='S' and x.stat='I' return r as ris" % i
			result=graph.cypher.execute(query)
			del arr[:]
			for r in result:
				arr.append(r.ris["duration"])
			if arr:
				prob= calculate_prob(arr)
				
				rand= random.random()
				if (rand > prob):
					change.append(i)		
		update_label(graph,change,t)
		apply_change(change,graph)
		vacc=stat(graph,change,t+1)
		
	crea_matrix_file(day_simu,perc)
	print "\n \n \n \n"

