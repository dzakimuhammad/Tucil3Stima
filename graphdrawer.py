import networkx as nx
import matplotlib.pyplot as plt

def drawgraph(parsed, path = None):
    G = nx.Graph()

    # kamus
    colored = False
    node = parsed[1]
    coor = parsed[2]
    adj = parsed[3]
    pos = {}
    
    # coloring
    nodecolor = []
    edgecolor = []
    pathcolor = []
    if path is not None:
        colored = True
        pathcolor = getedgefrompath(path)

    edgelabel = {}
    for i in range(len(adj)):
        if colored and node[i] in path:
            nodecolor.append("red")
        else:
            nodecolor.append("white")
            
        pos[node[i]] = (coor[i]["x"], coor[i]["y"])
        for j in range(len(adj[i])):
            if (i != j and i < j and adj[i][j] != 0):
                G.add_edge(node[i],node[j])
                if (node[i],node[j]) in pathcolor:
                    edgecolor.append("red")
                else:
                    edgecolor.append("black")
                    
                edgelabel[(node[i], node[j])] = '%.2f'%adj[i][j]
                
    pos = nx.planar_layout(G)
    nx.draw_planar(G, with_labels=True, node_color = nodecolor, edge_color = edgecolor, edgecolors = "black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edgelabel)

def getedgefrompath(path):
    out = []
    for i in range(len(path)-1):
      out.append((path[i], path[i+1]))
      out.append((path[i+1], path[i]))
    return out