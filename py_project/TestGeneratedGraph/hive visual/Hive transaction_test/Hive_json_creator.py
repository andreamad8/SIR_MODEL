def create_map_S(graph):
	map_file= open("map_S.txt","w")
	query= 'match (n {stat: "S"})-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()

def create_map_I(graph):
	map_file= open("map_I.txt","w")
	query= 'match (n {stat: "I"})-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()

def create_map_R(graph):
	map_file= open("map_R.txt","w")
	query= 'match (n {stat: "R"})-[r]-() return n.name as ris, count(r) as cnt order by cnt desc' 
	result=graph.cypher.execute(query)
	for r in result:
		map_file.write('%d \n' % r.ris)
	map_file.close()


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



def create_hive(change,arr_IR,graph):
	create_map_S(graph)
	for i in range(0,len(change)):
		pos=positio_map('map_S.txt',change[i])
		if pos is not None: 
			print ',\n{"x": 2, "y": 0.%d}' % pos
			print ',\n{"x": 0, "y": 0.%d}' % pos
			print ',\n{ "source": {"x": 2, "y": 0.%d}, "target" : {"x": 0, "y": 0.%d} }' % (pos, pos)

	create_map_I(graph)
	for i in range(0,len(arr_IR)):
		pos=positio_map('map_I.txt',arr_IR[i])
		if pos is not None: 
			print ',\n{"x": 0, "y": 0.%d}' % pos
			print ',\n{"x": 1, "y": 0.%d}' % pos
			print ',\n{ "source": {"x": 0, "y": 0.%d}, "target" : {"x": 1, "y": 0.%d} }' % (pos, pos)


 
from py2neo import Graph
import random
import json
graph = Graph()
change=[2]
arr_IR=[4]
create_hive(change,arr_IR,graph)

