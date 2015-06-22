#MATCH a  where not (s)-[:contact]-()
#create node 
def create_S( graph ):
	load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/flight/create_graph/Dataset/old/cordinat_nation.csv' AS csvLine CREATE (:country {country:csvLine.country, latitude: toFloat(csvLine.lat),longitude: toFloat(csvLine.lng)})"
	graph.cypher.execute(load)
	print "import nodes"


def create_rel( graph ):
	load="USING PERIODIC COMMIT 100 LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/flight/create_graph/Dataset/flight_c_to_c.csv' AS csvLine MATCH (a),(b) WHERE a.country = csvLine.country_departure and b.country= csvLine.country_arrival CREATE (a)-[r:flight]->(b) set r.num_pass=toInt(csvLine.number_of_people) return r"
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