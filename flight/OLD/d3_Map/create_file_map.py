from py2neo import Graph

graph = Graph()
file_out=open("C_to_C.json","w")
file_out.write("[")
results = graph.cypher.execute("MATCH (a)-[r]->(b) return a,b")
for r in results:
	file_out.write("{origin:{latitude:%.6f,longitude:%.6f},destination:{latitude:%.6f,longitude:%.6f}}, \n" % (r.a["latitude"],r.a["longitude"],r.b["latitude"],r.b["longitude"] ))
file_out.write("]")