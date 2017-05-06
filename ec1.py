x, y = raw_input().strip().split(" ")

graph = {}
source = ""
dest = ""
for i in range(int(y)+1):
	if i != int(y):
		u, v, w = raw_input().strip().split(" ")
		if graph.has_key(str(u)):
		    graph[u][v] = int(w)
		else:
		    graph[u] = {}
		    graph[u][v] = int(w)
	else:
		source, dest = raw_input().strip().split(" ")

d = {source: 0}

pathlist = []
def getPath(dest):
	if path.get(dest) is None:
		return pathlist.append(-1)
	if path.get(dest) == source:
		return pathlist
	pathlist.append(path.get(dest))
	return getPath(path.get(dest))

#print sorted(graph.items())
visited = []
path = {}
for nodes,edges in iter(sorted(graph.items())):
	#print edges
	minValue, minKey = min((v,k) for k,v in d.items() if k not in visited)
	if graph.get(str(minKey)) is None:
		break
	if minKey not in visited:
	    for neighbour, weight in graph.get(str(minKey)).iteritems():
		    #print neighbour, weight
		    adjacent = neighbour
		    if d.get(minKey) is not None:
		    	weight = d.get(minKey) + weight
		    #print str(minKey), d.get(minKey)
		    if adjacent not in d or weight < d.get(adjacent):
		        d[adjacent] =  weight
		        visited.append(minKey)
		        path[str(adjacent)] = minKey
		        #print path, d	    
#print path,d
final_path = getPath(dest)
if final_path is not None:
	print d.get(dest), len(final_path)+1
else:
	print -1, -1
