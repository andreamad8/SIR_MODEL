#create node 
def create_S( graph ):
	load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/Dataset2/Creat_set/nodes.csv' AS csvLine CREATE ({name: toInt( csvLine.id) , d_t: 0, stat: 'S' })"
	graph.cypher.execute(load)
	print "import nodes"



def create_rel( graph ):
	load="USING PERIODIC COMMIT 100 LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/Dataset2/Creat_set/edges.csv' AS csvLine MATCH (a),(b) WHERE a.name = toInt(csvLine.name_from) and b.name= toInt(csvLine.name_to) CREATE (a)-[r:contact]->(b) set r.duration= toInt(csvLine.duration) return r"
	graph.cypher.execute(load)


def delete(graph):
	graph.cypher.execute("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
	return

def show_graph(graph):
	results = graph.cypher.execute("MATCH (n) return n limit 30")
	print (results)
	results = graph.cypher.execute("MATCH (n)-[r]-() return r limit 30")
	print (results)
	return

def create_suplement_rel( graph ):
	for i in range(1,600):
		r1=random.randrange(0,1900)
		r2=random.randrange(0,1900)
		#d=random.randrange(1,2)
		query = 'MATCH (a),(b) WHERE a.name = %d and b.name= %d CREATE (a)-[r:contact]->(b) set r.duration= %d' % (r1, r2, 1)
		graph.cypher.execute(query)
	print("finish relation creations")
	return 


from py2neo import Graph
from py2neo.packages.httpstream import http
import random
http.socket_timeout = 9999
graph = Graph()
#delete(graph)
#create_S(graph)
#create_rel(graph)
create_suplement_rel( graph )
show_graph(graph)

