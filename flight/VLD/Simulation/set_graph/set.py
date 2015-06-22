def create_I(graph):
	country="Italy"
	query="MATCH (n) WHERE n.country = '%s' and n.stat='S' SET n.stat='I' set n.I=100" % country
	graph.cypher.execute(query)
	return

def reset_label(graph):
	query="MATCH n set n.stat='S'" 
	graph.cypher.execute(query)
	return

def set_population(graph):
	query="MATCH n set n.S=10000 set n.I=0 set n.R=0" 
	graph.cypher.execute(query)
	return

from py2neo import Graph
from random import randint
graph = Graph()
set_population(graph)
reset_label(graph)
create_I(graph)
