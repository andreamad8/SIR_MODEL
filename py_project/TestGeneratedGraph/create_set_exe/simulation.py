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

from py2neo import Graph
import random
import json
from function import * 

change=list()
arr=list()
day_simu=20;
Matrix = [[0 for y in xrange(3)] for x in xrange(day_simu+1)]
graph = Graph()
result=graph.cypher.execute("MATCH (n) return count(n) as ris")
nodes=print_single(result)
print "Number of nodes: %d" % nodes

stat(graph,"",0)
create_map(graph)

for t in range(0,day_simu):
	
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
			if (rand < prob):
				change.append(i)
	
	hive_plot_entire_graph(t,graph)			
	update_label(graph,change,t)
	apply_change(change,graph)
	stat(graph,change,t+1)
	


crea_matrix_file(day_simu)

