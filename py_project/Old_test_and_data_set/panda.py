#%matplotlib inline
%load_ext cypher
results = %cypher MATCH (a)-[]-(b) RETURN a, b
import networkx as nx
ris=results.graph
#nx.draw(ris)

nx.draw_networkx(ris,pos=nx.spring_layout(ris,iterations=10,scale=1000),with_labels=False,node_size=100,width=0.1)
nx.draw_networkx_edges(ris,pos=nx.spring_layout(ris,iterations=10,scale=1000),alpha=0.3,width=0.1, edge_color='m')
nx.draw_networkx_nodes(ris,pos=nx.spring_layout(ris,iterations=10,scale=1000),node_size=100,node_color='w',alpha=0.4)
nx.draw_networkx_edges(ris,pos=nx.spring_layout(ris,iterations=10,scale=1000),alpha=0.4,node_size=0,width=1,edge_color='k')
nx.draw_networkx_labels(ris,pos=nx.spring_layout(ris,iterations=10,scale=1000),fontsize=14)