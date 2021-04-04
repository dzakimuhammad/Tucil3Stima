import astar, graphdrawer, util

parsed = None
type = 0

def start(filename = None):
    if filename is None:
        filename = input("Masukkan nama file: ")
    
    global parsed
    parsed = util.parse(filename)

    print()
    print("Visualisasi graf masukan (bobot dalam km): ")
    graphdrawer.drawgraph(type, parsed)

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
        graphdrawer.drawgraph(type, parsed, searchPath)
    else:
        print("No path found")

def setgraphtype(tipe):
    if tipe == -1 or tipe == 0 or tipe == 1 or tipe == 2 or tipe == 3 or tipe == 4:
        # type = tipe graf
        # -1 = default (pake x y)
        # 0 = planar
        # 1 = circular
        # 2 = spectral
        # 3 = spring
        # 4 = shell
        # 5 = random
        name = ["default", "planar", "circular", "spectral", "spring", "shell"]
        global type
        type = tipe
        print("Graph type:", name[tipe+1])
    else:
        raise Exception("Wrong type")