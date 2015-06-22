def print_single(result):
	for r in result:
		out= r.ris
	return out

def stat(graph,change):
	result=graph.cypher.execute("MATCH (n:S) return count(n) as ris")
	out=print_single(result)
	print "Number of S: %d" % out

	result=graph.cypher.execute("MATCH (n:I) return count(n) as ris")
	out=print_single(result)
	print "Number of I: %d" % out

	result=graph.cypher.execute("MATCH (n:R) return count(n) as ris")
	out=print_single(result)
	print "Number of R: %d" % out
	print "Number of change: %d" % len(change)
	print change
	print ""

def calculate_prob(arr):
	r=0.07
	ris=1
	for i in range(0,len(arr)):
		ris=ris * (1-pow((1-r), arr[i]))	
	return ris

def apply_change(change,graph):
	for i in range(0,len(change)):
		query= "MATCH (n:S {id : '%d'}) REMOVE n:S SET n:I " % change[i]
		result=graph.cypher.execute(query)

def update_label(graph):
	query = 'MATCH (n:I) set n.d_t=n.d_t+1 return n as ris'
	result=graph.cypher.execute(query)
	arr_id=list()
	arr_time=list()
	for r in result:
		arr_id.append(r.ris["id"])
		arr_time.append(r.ris["d_t"])

	for i in range(0,len(arr_id)):
		if(arr_time[i]>3):
			query = "MATCH (n:I {id:'%s'}) REMOVE n:I SET n:R " % arr_id[i]
 			result=graph.cypher.execute(query)


from py2neo import Graph
import random
change=list()
arr=list()
graph = Graph()
result=graph.cypher.execute("MATCH (n) return count(n) as ris")
nodes=print_single(result)
print "Number of nodes: %d" % nodes

stat(graph,"")

for t in range(1,7):
	del change[:]
	for i in range(1,nodes):
		query= "MATCH (n:S {id : '%d' })-[r:contact]-(x:I) return r as ris" % i
		result=graph.cypher.execute(query)
		del arr[:]
		for r in result:
			arr.append(r.ris["duration"])
		if arr:
			prob= calculate_prob(arr)
			
			rand= random.random()
			if (rand > prob):
				
				change.append(i)
	apply_change(change,graph)
	update_label(graph)
	stat(graph,change)
