import astar, graphdrawer, util

parsed = None

def start(filename = None):
    if filename is None:
        filename = input("Masukkan nama file: ")
    
    global parsed
    parsed = util.parse(filename)
    graphdrawer.drawgraph(parsed)

def process(startNode = None, goalNode = None):
    if startNode is None or goalNode is None:
        startNode = input("Simpul awal: ")
        goalNode = input("Simpul tujuan: ")
    
    heuristic = astar.heuristics_distance(parsed, startNode, goalNode)
    searchPath = astar.astar_search(parsed, heuristic, startNode, goalNode)

    if searchPath is not None:
        graphdrawer.drawgraph(parsed, searchPath)
    else:
        print("No path found")