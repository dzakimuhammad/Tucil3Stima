from math import sqrt
from operator import itemgetter

def tetangga(id, graph):
  ttg = []
  for i, adj in enumerate(graph[id]):
    if adj != 0:
      ttg.append(i)
  return ttg

def parse(nama_file):
  file = open(nama_file, "r")
  
  lines = file.readlines()
  lineslen = len(lines)
  node = []
  coor = []
  adj = []
  
  print("Removing new line..")
  for i in range(lineslen):
    lines[i] = lines[i].replace("\n", "")

  nodetotal = int(lines[0])

  print("Getting the coordinates..")
  for i in range(1, nodetotal+1):
    split = lines[i].split(" ")
    node.append(split[0])
    coor.append({
      "x": float(split[1]),
      "y": float(split[2])
    })
  
  print("Getting the adj matrix..")
  for i in range(nodetotal+1, lineslen):
    split = lines[i].split(" ")
    row = []
    for jarak in split:
      row.append(int(jarak))
    adj.append(row)

  print("Parsing", nama_file, "is done")

  listnode = {}

  for i in range(len(node)):
    ttg = []
    for nodeid in tetangga(i, adj):
      distance = sqrt((coor[i]["x"]-coor[nodeid]["x"])**2 + (coor[i]["y"]-coor[nodeid]["y"])**2)
      ttg.append((node[nodeid], distance))
      adj[i][nodeid] = distance
    ttg = sorted(ttg, key=itemgetter(1))
    listnode[node[i]] = ttg
  
  return listnode, node, coor, adj

# access parsed
# parsed[0] = graph
# parsed[1] = list node (string)
# parsed[2] = list coordinate
# parsed[3] = adj matrix with distance
# tes
'''
parsed = parse("tes.txt")
print(parsed)
'''