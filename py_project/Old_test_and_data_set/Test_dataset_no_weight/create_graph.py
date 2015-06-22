def create_S( graph ):
	load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/py_project/person.csv' AS csvLine CREATE (p:S { id : csvLine.name , name: csvLine.id, age: csvLine.AGE, d_t: 0 })"
	graph.cypher.execute(load)
	print("finish node creatations")
	#tx = graph.cypher.begin()
	#statement = "create (a :S {name : {name}, age: {age}, d_t : {d_t}})"
	#tx.append(statement, {"name": 1, "age": 20, "d_t":0})
	#tx.append(statement, {"name": 2, "age": 20, "d_t":0})
	#tx.commit()
	#return 

def create_rel( graph ):
	load="USING PERIODIC COMMIT 100 LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/py_project/ping.csv' AS csvLine MATCH (a),(b) WHERE a.name = csvLine.ID and b.name=csvLine.TO_ID CREATE (a)-[r:contact]->(b) set r.duration= 10 return r"
	graph.cypher.execute(load)
	print("finish relation creations")
	#tx = graph.cypher.begin()
	#statement = "MATCH (a),(b) WHERE a.name = {name_1} and b.name={name_2} CREATE (a)-[r:contact]->(b) set r.duration= {dur}"
	#tx.append(statement, {"name_1": 1, "name_2": 2, "dur": 10})
	#tx.commit()
	return 


def delete(graph):
	graph.cypher.execute("MATCH (n:S) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
	return

def show_graph(graph):
	results = graph.cypher.execute("MATCH (n:S) return n")
	print (results)
	return

from py2neo import Graph
from py2neo.packages.httpstream import http
http.socket_timeout = 9999
graph = Graph()
delete(graph)
create_S(graph)
create_rel(graph)
#show_graph(graph)

