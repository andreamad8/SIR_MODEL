def print_single(result):
	for r in result:
		out= r.ris
	return out


def calculate_prob(arr):
	
	dur=0
	for i in range(0,len(arr)):
		dur=dur+ arr[i]

	return dur


def apply_change(change,graph,change_Json):
	for i in range(0,len(change)):
		num_I=int(change[i][1]*1000)
		query= "MATCH (n) where id(n)=%d and n.stat='S' SET n.stat='I' set n.I=%d return n as ris" % (change[i][0],num_I)
		result=graph.cypher.execute(query)

			

	


			
			
			


def update_label(graph,change,t):
	query = "MATCH (n) where n.stat='I' set n.d_t=n.d_t+1 return n as ris"
	result=graph.cypher.execute(query)
	arr_id=list()
	arr_time=list()
	for r in result:
		arr_id.append(r.ris["name"])
		arr_time.append(r.ris["d_t"])
	for i in range(0,len(arr_id)):
		if(arr_time[i]>4):
			query = "MATCH (n {name: %s}) where n.stat='I' SET n.stat='R'" % arr_id[i]
 			result=graph.cypher.execute(query)