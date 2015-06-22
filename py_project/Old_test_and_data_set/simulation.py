

def print_single(result):
	for r in result:
		out= r.ris
	return out

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

def calculate_prob(arr):
	r=0.2
	ris=1
	for i in range(0,len(arr)):
		ris=ris * (1-pow((1-r), arr[i]))	
	return ris

def apply_change(change,graph):
	for i in range(0,len(change)):
		query= "MATCH (n {name : %d}) where n.stat='S' SET n.stat='I'" % change[i]
		result=graph.cypher.execute(query)





def create_map(graph):
	map_file= open("map.txt","w")
	query= 'match (n)-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()

def create_map_tot(graph):
	map_file= open("map.txt","w")
	query= 'match (n)-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()


def positio_map(file_in,ris):
	cnt=1
	datafile = file(file_in) 
	for line in datafile:
		if int(ris) == int(line):
			return cnt
		cnt=cnt+1

def hive_plot_entire_graph(t):

	from py2neo import Graph
	import json
	graph = Graph()

	file_nodes="nodes_full_graph/nodes%d.json" %t
	out_nodes = open(file_nodes,"w")
	out_nodes.write('[\n')


	file_links="links_full_graph/links%d.json" %t
	out_link = open(file_links,"w")

	out_link.write('[\n')

	create_map_tot(graph)

	#creation nodes in json file nodest
	query= 'match (a) where a.stat="S" return a.name as ris'
	result=graph.cypher.execute(query)
	i=1
	for r in result:
		pos=positio_map('map.txt',r.ris)
		if(i==1):
			out_nodes.write('{"x": 2, "y": 0.%d}' % pos)
			i=i+1
		else:	
			out_nodes.write(',\n{"x": 2, "y": 0.%d}' % pos)

	query= 'match (a) where a.stat="I" return a.name as ris'
	result=graph.cypher.execute(query)

	for r in result:
		pos=positio_map('map.txt',r.ris)
		if (i==1):
			out_nodes.write( '{"x": 0, "y": 0.%d}' % pos)
			i=i+1
		else:
			out_nodes.write( ',\n{"x": 0, "y": 0.%d}' % pos)

	query= 'match (a) where a.stat="R" return a.name as ris'
	result=graph.cypher.execute(query)


	for r in result:
		pos=positio_map('map.txt',r.ris)
		if (i==1):
			out_nodes.write( '{"x": 1, "y": 0.%d}' % pos)
			i=i+1
		else:
			out_nodes.write( ',\n{"x": 1, "y": 0.%d}' % pos)


	out_nodes.write(']')
	#finish creation

	#create edge in the links file


	#the edge I -- S
	query= 'match (a)-[r]->(b) where a.stat="I" and b.stat= "S" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	i=1
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 2, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 2, "y": 0.%d} }' % (pos_source, pos_target) )

	#the edge R -- I
	query= 'match (a)-[r]->(b) where a.stat="R" and b.stat= "I" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos_source, pos_target) )


	#the edge S -- R
	query= 'match (a)-[r]->(b) where a.stat="S" and b.stat= "R" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos_source, pos_target) )


	out_link.write(']')


	out_nodes.close()
	out_link.close()


def positio_map(file_in,ris):
	cnt=1
	datafile = file(file_in) 
	for line in datafile:
		if int(ris) == int(line):
			return cnt
		cnt=cnt+1

def create_hive(change,arr_IR,graph,t):
	file_node_t= "nodes/nodes%d.json" % t
	out_nodes = open(file_node_t,"w")

	out_nodes.write('[')
	file_links_t= "links/links%d.json" % t
	out_link = open(file_links_t,"w")

	out_link.write('[')
	cnt=1
	create_map(graph)
	for i in range(0,len(change)):
		pos=positio_map('map.txt',change[i])
		if pos is not None:
			if cnt==1: 
				out_nodes.write('\n{"x": 2, "y": 0.%d}' % pos)
				out_nodes.write(',\n{"x": 0, "y": 0.%d}' % pos)
				out_link.write('\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos, pos))
				cnt=2
			else:
				out_nodes.write(',\n{"x": 2, "y": 0.%d}' % pos)
				out_nodes.write(',\n{"x": 0, "y": 0.%d}' % pos)
				out_link.write(',\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos, pos))

	for i in range(0,len(arr_IR)):
		pos=positio_map('map.txt',arr_IR[i])
		if pos is not None:
			if cnt==2: 
				out_nodes.write(',\n{"x": 0, "y": 0.%d}' % pos)
				out_nodes.write(',\n{"x": 1, "y": 0.%d}' % pos)
				out_link.write( ',\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos, pos))
			else:
				out_nodes.write('\n{"x": 0, "y": 0.%d}' % pos)
				out_nodes.write(',\n{"x": 1, "y": 0.%d}' % pos)
				out_link.write( '\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos, pos))
				cnt=2
	
	out_nodes.write(']')
	out_link.write(']')
	out_nodes.close()
	out_link.close()


def update_label(graph,change,t):
	query = "MATCH (n) where n.stat='I' set n.d_t=n.d_t+1 return n as ris"
	result=graph.cypher.execute(query)
	arr_id=list()
	arr_time=list()
	for r in result:
		arr_id.append(r.ris["name"])
		arr_time.append(r.ris["d_t"])
	arr_IR=list()
	for i in range(0,len(arr_id)):
		if(arr_time[i]>4):
			arr_IR.append(arr_id[i])
			query = "MATCH (n {name: %s}) where n.stat='I' SET n.stat='R'" % arr_id[i]
 			result=graph.cypher.execute(query)
 	create_hive(change,arr_IR,graph,t)



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
change=list()
arr=list()
day_simu=20;
Matrix = [[0 for y in xrange(3)] for x in xrange(day_simu+1)]
graph = Graph()
result=graph.cypher.execute("MATCH (n) return count(n) as ris")
nodes=print_single(result)
print "Number of nodes: %d" % nodes

stat(graph,"",0)


for t in range(0,day_simu):
	del change[:]
	for i in range(1,nodes):
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
	hive_plot_entire_graph(t)			
	update_label(graph,change,t)
	apply_change(change,graph)
	stat(graph,change,t+1)
	


crea_matrix_file(day_simu)

