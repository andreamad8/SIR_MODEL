def create_map_tot(graph):
	map_file= open("map.txt","w")
	query= 'match (n)-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()


def positio_map(file_in,ris):
	cnt=1
	datafile = file(file_in) 
	for line in datafile:
		if int(ris) == int(line):
			return cnt
		cnt=cnt+1


def hive_plot_entire_graph(t):

	from py2neo import Graph
	import json
	graph = Graph()

	file_nodes="nodes%d.json" %t
	out_nodes = open(file_nodes,"w")
	out_nodes.write('[\n')


	file_links="links%d.json" %t
	out_link = open(file_links,"w")

	out_link.write('[\n')

	create_map_tot(graph)

	#creation nodes in json file nodest
	query= 'match (a) where a.stat="S" return a.name as ris'
	result=graph.cypher.execute(query)
	i=1
	for r in result:
		pos=positio_map('map.txt',r.ris)
		if(i==1):
			out_nodes.write('{"x": 2, "y": 0.%d}' % pos)
			i=i+1
		else:	
			out_nodes.write(',\n{"x": 2, "y": 0.%d}' % pos)

	query= 'match (a) where a.stat="I" return a.name as ris'
	result=graph.cypher.execute(query)

	for r in result:
		pos=positio_map('map.txt',r.ris)
		if (i==1):
			out_nodes.write( '{"x": 0, "y": 0.%d}' % pos)
			i=i+1
		else:
			out_nodes.write( ',\n{"x": 0, "y": 0.%d}' % pos)

	query= 'match (a) where a.stat="R" return a.name as ris'
	result=graph.cypher.execute(query)


	for r in result:
		pos=positio_map('map.txt',r.ris)
		if (i==1):
			out_nodes.write( '{"x": 1, "y": 0.%d}' % pos)
			i=i+1
		else:
			out_nodes.write( ',\n{"x": 1, "y": 0.%d}' % pos)


	out_nodes.write(']')
	#finish creation

	#create edge in the links file


	#the edge I -- S
	query= 'match (a)-[r]->(b) where a.stat="I" and b.stat= "S" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	i=1
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 2, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 2, "y": 0.%d} }' % (pos_source, pos_target) )

	#the edge R -- I
	query= 'match (a)-[r]->(b) where a.stat="R" and b.stat= "I" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 1, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos_source, pos_target) )


	#the edge S -- R
	query= 'match (a)-[r]->(b) where a.stat="S" and b.stat= "R" return a.name as source, b.name as target '
	result=graph.cypher.execute(query)
	arr_time=list()
	for r in result:
		pos_source=positio_map('map.txt',r.source)
		pos_target=positio_map('map.txt',r.target)
		if(i==1):
			out_link.write('{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos_source, pos_target) )
			i=i+1
		else:
			out_link.write(',\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos_source, pos_target) )


	out_link.write(']')


	out_nodes.close()
	out_link.close()

hive_plot_entire_graph(0)
