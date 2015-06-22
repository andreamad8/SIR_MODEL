#create node 
def create_S( graph ):
	#load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/py_project/person.csv' AS csvLine CREATE (p:S { id : csvLine.name , name: csvLine.id, age: csvLine.AGE, d_t: 0 })"
	#graph.cypher.execute(load)

	for i in range(1,301):
		query = "create (a  {name : %d, d_t : 0, stat : 'S' })" % i
		graph.cypher.execute(query)

	print("finish node creatations")
	#return 

def create_rel( graph ):
	#load="USING PERIODIC COMMIT 100 LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/py_project/ping.csv' AS csvLine MATCH (a),(b) WHERE a.name = csvLine.ID and b.name=csvLine.TO_ID CREATE (a)-[r:contact]->(b) set r.duration= 10 return r"
	#graph.cypher.execute(load)

	for i in range(1,901):
		r1=random.randrange(1,301)
		r2=random.randrange(1,301)
		d=random.randrange(1,20)
		query = 'MATCH (a),(b) WHERE a.name = %d and b.name= %d CREATE (a)-[r:contact]->(b) set r.duration= %d' % (r1, r2, d)
		graph.cypher.execute(query)
	print("finish relation creations")
	return 


def delete(graph):
	graph.cypher.execute("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
	return

def show_graph(graph):
	results = graph.cypher.execute("MATCH (n) return n")
	print (results)
	return

from py2neo import Graph
from py2neo.packages.httpstream import http
import random
http.socket_timeout = 9999
graph = Graph()
delete(graph)
create_S(graph)
create_rel(graph)
show_graph(graph)

