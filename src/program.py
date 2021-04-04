import astar, graphdrawer, util

parsed = None

def start(filename = None):
    if filename is None:
        filename = input("Masukkan nama file: ")
    
    global parsed
    parsed = util.parse(filename)

    print()
    print("Visualisasi graf masukan (bobot dalam km): ")
    graphdrawer.drawgraph(parsed)

def process(startNode = None, goalNode = None):
    if startNode is None or goalNode is None:
        startNode = input("Simpul awal: ")
        goalNode = input("Simpul tujuan: ")
    
    heuristic = astar.heuristics_distance(parsed, startNode, goalNode)
    searchPath = astar.astar_search(parsed, heuristic, startNode, goalNode)

    if searchPath is not None:
        print()
        print("Hasil: ")
        distance = util.getdistancefrompath(searchPath, parsed)
        print("Jarak terpendek dari", startNode, "dan", goalNode, "adalah", '%.2f'%distance, "km")
        graphdrawer.drawgraph(parsed, searchPath)
    else:
        print("No path found")