def create_I(graph,n):
	for x in xrange(0,n):
		rand=randint(1,31)
		query="MATCH (n) WHERE n.name = %d and n.stat='S' SET n.stat='I'" % rand
		graph.cypher.execute(query)
	return

def reset_label(graph):
	query="MATCH n set n.d_t=0 set n.stat='S'" 
	graph.cypher.execute(query)
	return

from random import randint