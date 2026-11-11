import networkx as nx 
import matplotlib.pyplot as plt 
G = nx.Graph() 
G.add_weighted_edges_from([ 
    ('A', 'B', 2), 
    ('A', 'C', 4), 
    ('B', 'D', 3), 
    ('B', 'E', 5), 
    ('C', 'F', 2), 
    ('D', 'G', 4), 
    ('E', 'G', 2), 
    ('F', 'G', 3) 
]) 
pos = { 
'A': (0, 3), 
'B': (-1, 2), 
'C': (1, 2), 
'D': (-1.5, 1), 
'E': (-0.5, 1), 
'F': (1, 1), 
'G': (0, 0) 
} 
nx.draw( 
G, 
pos, 
with_labels=True, 
node_size=1800, 
font_size=12 
)
cost_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels( 
G, 
pos,
   edge_labels=cost_labels, 
    font_size=10 
) 
plt.show() 