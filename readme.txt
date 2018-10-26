Requirements to run python program:
pandas
numpy
matplotlib
geopandas
osmnx
networkX

Here, We imported the the map from Open Street Maps and take two nodes randomly as source and destination and found the paths between them
and used matplotlib to implement in the graph. As this is a prototype, our future work will include as follwos:

			--------------------------------FUTURE WORK------------------------------------------

As we found the paths between source and destination which are randomly selected, we will do this for specific source and destinastion
and 
based on the paths we got and the information of GPS we will get to know the affected paths (finding the affected path is: we will 
send our
rescue team to all the paths we found and get the information from them). From the remaining paths we will get to know the
properties like 
distance, type of road(National Highways or State Highways or Normal), Based on this information we will send our rescue vehicle.