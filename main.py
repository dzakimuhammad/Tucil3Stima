from util import parse
from astar import heuristics_distance, astar_search
parsed = parse("tes.txt")
print(parsed[0])
print(parsed[1])
print(parsed[2])
print(parsed[3])
startNode = input("Simpul awal: ")
goalNode = input("Simpul tujuan: ")
heuristic = heuristics_distance(parsed, startNode, goalNode)
searchPath = astar_search(parsed, heuristic, startNode, goalNode)
print(searchPath)