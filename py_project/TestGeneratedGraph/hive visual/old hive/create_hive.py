from py2neo import Graph
import json
graph = Graph()

out_nodes = open("nodes.json","w")

out_nodes.write('[\n')

out_link = open("links.json","w")

out_link.write('[\n')


#creation nodes in json file
query= 'match (a) where a.stat="S" return id(a) as ris'
result=graph.cypher.execute(query)
i=1
arr_time=list()
for r in result:
	if(i==1):
		out_nodes.write('{"x": 0, "y": 0.%d}' % r.ris)
		i=i+1
	else:	
		out_nodes.write(',\n{"x": 0, "y": 0.%d}' % r.ris)

query= 'match (a) where a.stat="I" return id(a) as ris'
result=graph.cypher.execute(query)

arr_time=list()
for r in result:
	out_nodes.write( ',\n{"x": 1, "y": 0.%d}' % r.ris)

query= 'match (a) where a.stat="R" return id(a) as ris'
result=graph.cypher.execute(query)

arr_time=list()
for r in result:
	out_nodes.write( ',\n{"x": 2, "y": 0.%d}' % r.ris)


out_nodes.write(']')
#finish creation

#create edge in the links file

#the edge S -> I
'''query= 'match (a)-[r]->(b) where a.stat="S" and b.stat= "I" return id(a) as source, id(b) as target  '
result=graph.cypher.execute(query)
i=1
arr_time=list()
for r in result:
	if(i==1):
		out_link.write('{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (r.source, r.target) )
		i=i+1
	else:	
		out_link.write(',\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (r.source, r.target) )
'''
#the edge I -> S
query= 'match (a)-[r]->(b) where a.stat="I" and b.stat= "S" return id(a) as source, id(b) as target '
result=graph.cypher.execute(query)
i=1
arr_time=list()
for r in result:
	if(i==1):
		out_link.write('{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (r.source, r.target) )
		i=i+1
	else:
		out_link.write(',\n{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (r.source, r.target) )

#first the edge R -> I
query= 'match (a)-[r]->(b) where a.stat="R" and b.stat= "I" return id(a) as source, id(b) as target '
result=graph.cypher.execute(query)
arr_time=list()
for r in result:
	out_link.write(',\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (r.source, r.target) )



out_link.write(']')


out_nodes.close()
out_link.close()