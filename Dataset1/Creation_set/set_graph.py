def create_I(graph,n):
	for x in xrange(0,n):
		rand=randint(1,1589)
		query="MATCH (n) WHERE n.name = %d and n.stat='S' SET n.stat='I'" % rand
		graph.cypher.execute(query)
	return

def reset_label(graph):
	query="MATCH n set n.d_t=0 set n.stat='S'" 
	graph.cypher.execute(query)
	return

from py2neo import Graph
from random import randint
graph = Graph()
reset_label(graph)
create_I(graph,80)
