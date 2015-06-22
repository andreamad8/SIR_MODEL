from py2neo import Graph
import json
graph = Graph()

out_file = open("grafo5.json","w")
out_file.write('{"nodes":[\n')

#query= 'match (a)-[r]->(b) with distinct a,r,b return {id: toInt(a.name), name: a.name, d_t: a.d_t, label: labels(a)} as ris'

query= 'match (a) with distinct a return {name: a.name,  d_t: a.d_t, label: a.stat } as ris'
result=graph.cypher.execute(query)
i=1
arr_time=list()
for r in result:
	if(i==1):
		out_file.write('%s'%json.dumps(r.ris))
		i=i+1
	else:
		out_file.write(',\n%s'%json.dumps(r.ris))
out_file.write('],\n  "links":[\n')
#query= "match (a)-[r]->(b) with distinct a, b,r return {source: toInt(b.name), target: toInt(a.name), duration: r.duration} as ris"

query= "MATCH (a)-[r]->(b)  return { duration: r.duration, target: toInt(b.name)-1, source: toInt(a.name)-1} as ris"
result=graph.cypher.execute(query)
j=1
arr_time=list()
for r in result:
	if (j==1):
		out_file.write('%s'%json.dumps(r.ris))
		j=j+1
	else:
		out_file.write(',\n%s'%json.dumps(r.ris))
out_file.write('\n]}')
out_file.close()

