#MATCH a  where not (s)-[:contact]-()
#create node 
def create_S( graph ):
	load="LOAD CSV WITH HEADERS FROM 'file:c:/Users/andrea/Desktop/flight/create_graph/Dataset/Openflight/airports.csv' AS csvLine CREATE (:airport {airport_id:csvLine.id, name:csvLine.Name,city: csvLine.City, country: csvLine.Country,IATA: csvLine.IATA, latitude: toFloat(csvLine.Latitude),longitude: toFloat(csvLine.Longitude)})"
	graph.cypher.execute(load)
	print "import nodes"



def create_rel( graph ):
	import csv
	f = open('edge.csv')
	csv_f = csv.reader(f)
	for row in csv_f:
		load="MATCH (a),(b) WHERE a.IATA = '%s' and b.IATA= '%s' CREATE (a)-[r:flight]->(b) set r.num_pass = toInt(%s) return r"% (row[0],row[1],row[2])
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

graph = Graph()
delete(graph)
create_S(graph)
create_rel(graph)
show_graph(graph)

