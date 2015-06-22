from py2neo import Graph

graph = Graph()
file_out=open("globe.json","w")
file_out.write("[")
results = graph.cypher.execute("MATCH (a)-[r]->(b) where r.num_pass > 700000 return a,b")
ind=0
for r in results:
	if(ind==0):
		file_out.write('{"origin":{"latitude":%.6f,"longitude":%.6f},"destination":{"latitude":%.6f,"longitude":%.6f}}' % (r.a["latitude"],r.a["longitude"],r.b["latitude"],r.b["longitude"] ))
		ind=1
	else:
		file_out.write(', \n{"origin":{"latitude":%.6f,"longitude":%.6f},"destination":{"latitude":%.6f,"longitude":%.6f}}' % (r.a["latitude"],r.a["longitude"],r.b["latitude"],r.b["longitude"] ))
file_out.write("]")