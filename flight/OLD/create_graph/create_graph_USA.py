#MATCH a  where not (s)-[:contact]-()
#create node 
def create_S( graph ):
	load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/flight/create_graph/Dataset/usa.csv' AS csvLine CREATE (:airport {city: csvLine.city,latitude: toFloat(csvLine.lat),longitude: toFloat(csvLine.lng)})"
	graph.cypher.execute(load)
	print "import nodes"



def create_rel( graph ):
	load="USING PERIODIC COMMIT 100 LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/flight/create_graph/Dataset/usa_air.csv' AS csvLine MATCH (a),(b) WHERE a.city = csvLine.city_O and b.city= csvLine.city_D CREATE (a)-[r:flight]->(b) return r"
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


from py2neo import Graph
from py2neo.packages.httpstream import http
import random
http.socket_timeout = 9999
graph = Graph()
delete(graph)
create_S(graph)
create_rel(graph)
show_graph(graph)

