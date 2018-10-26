

#------------------------------------------Prototype of our idea-----------------------------------------------------


import osmnx as ox

import networkx as nx

import geopandas as gpd

import matplotlib.pyplot as plt

import pandas as pd


'''-------------------------------------------------> importing Open street maps to python fo find the paths 
													  between to source and destinastion '''

place_name = "Kamppi, Helsinki, Finland"

graph = ox.graph_from_place(place_name, network_type='drive')


graph_proj = ox.project_graph(graph)




nodes_proj, edges_proj = ox.graph_to_gdfs(graph_proj, nodes=True, edges=True)


from shapely.geometry import box

bbox = box(*edges_proj.unary_union.bounds)

'''----------------------------------------------> findind random source and destination '''

orig_point = bbox.centroid


nodes_proj['x'] = nodes_proj.x.astype(float)

maxx = nodes_proj['x'].max()

target_loc = nodes_proj.loc[nodes_proj['x']==maxx, :]


target_point = target_loc.geometry.values[0]


orig_xy = (orig_point.y, orig_point.x)

target_xy = (target_point.y, target_point.x)

orig_node = ox.get_nearest_node(graph_proj, orig_xy, method='euclidean')

target_node = ox.get_nearest_node(graph_proj, target_xy, method='euclidean')

o_closest = nodes_proj.loc[orig_node]

t_closest = nodes_proj.loc[target_node]


'''----------------------------------------------------> finding all the paths between two nodes (source and destination) which are 
randomly selected as this is the prototype of our idea'''

count=0
route=[]
for path in nx.all_simple_paths(G=graph_proj, source=orig_node, target=target_node):
	# print(path)
	route.append(path)
	if count == 10:
		break
	count+=1



# ----------------------------------------------------------------> plottina graph for visualization


ec= ox.get_edge_colors_by_attr(graph_proj, attr='length')
# ox.set_title("new1")
ox.plot_graph(graph_proj, edge_color=ec)



fig, ax = ox.plot_graph_routes(graph_proj, route,edge_color='#ffffff')


plt.title("Different paths between source and destination")
plt.tight_layout()

#--------------------------------------------------------------------->Future work<-------------------------------------------------

'''


As we found the paths between source and destination which are randomly selected, we will do this for specific source and destinastion
and based on the paths we got and the information of GPS we will get to know the affected paths (finding the affected path is: we will 
send our rescue team to all the paths we found and get the information from them). From the remaining paths we will get to know the
properties like distance, type of road(National Highways or State Highways or Normal), Based on this information we will send our rescue vehicle. 


'''











