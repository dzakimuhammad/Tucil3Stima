import networkx as nx
import matplotlib.pyplot as plt

def drawgraph(type, parsed, path = None):
    # reference = https://networkx.org/documentation/stable/reference/drawing.html

    # kamus
    G = nx.Graph()
    colored = False
    node = parsed[1]
    coor = parsed[2]
    adj = parsed[3]

    pos = {} # buat posisi graf (x,y) kalo dipake
    edgelabel = {} # buat label jarak
    
    # coloring
    # reference: https://stackoverflow.com/questions/25639169/networkx-change-color-width-according-to-edge-attributes-inconsistent-result
    #            https://stackoverflow.com/questions/27030473/how-to-set-colors-for-nodes-in-networkx

    nodecolor = []
    #edgecolor = []
    pathcolor = []
    if path is not None:
        colored = True
        pathcolor = getedgefrompath(path)
    
    # iterasi buat assign graf ke visualizer
    for i in range(len(adj)):        
        # assign posisi graf dari input ke visualizer
        pos[node[i]] = (coor[i]["x"], coor[i]["y"])
        for j in range(len(adj[i])):
            if (i != j and i < j and adj[i][j] != 0):
                # assign warna edge
                color = None
                if (node[i],node[j]) in pathcolor:
                    #edgecolor.append("red")
                    color = "red"
                else:
                    #edgecolor.append("black")
                    color = "black"
                
                # assign edge ke visualizer
                G.add_edge(node[i],node[j],color=color)
                edgelabel[(node[i], node[j])] = '%.2f'%adj[i][j]
    
    for node in G:
        # assign warna node
        if colored and node in path:
            nodecolor.append("red")
        else:
            nodecolor.append("white")

    # type = tipe graf
    # -1 = default (pake x y)
    # 0 = planar
    # 1 = circular
    # 2 = spectral
    # 3 = spring
    # 4 = shell

    options = {
        "with_labels": True,
        "node_color": nodecolor,
        "edge_color": [G[i][j]['color'] for i,j in G.edges()],
        "edgecolors": "black"
    }

    if type == -1:
        nx.draw_networkx(G, pos, **options)
    elif type == 0:
        pos = nx.planar_layout(G)
        nx.draw_planar(G, **options)
    elif type == 1:
        pos = nx.circular_layout(G)
        nx.draw_circular(G, **options)
    elif type == 2:
        pos = nx.spectral_layout(G)
        nx.draw_spectral(G, **options)
    elif type == 3:
        pos = nx.spring_layout(G)
        nx.draw_spring(G, **options)
    elif type == 4:
        pos = nx.shell_layout(G)
        nx.draw_shell(G, **options)
                
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edgelabel)
    
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()

def getedgefrompath(path):
    out = []
    for i in range(len(path)-1):
      out.append((path[i], path[i+1]))
      out.append((path[i+1], path[i]))
    return out