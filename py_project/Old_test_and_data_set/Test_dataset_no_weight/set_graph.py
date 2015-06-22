def create_I(graph,n):
	for x in xrange(0,n):
		rand=randint(1,700)
		query="MATCH (n) WHERE n.id = '%d' REMOVE n:S SET n:I" % rand
		graph.cypher.execute(query)
	return
def reset_label(graph):
	query="MATCH n where n:I OR n:R REMOVE n:I REMOVE n:R SET n:S set n.d_t=0" 
	graph.cypher.execute(query)
	return

from py2neo import Graph
from random import randint
graph = Graph()
reset_label(graph)
create_I(graph,40)
