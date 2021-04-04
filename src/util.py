from math import sqrt, cos, sin, pi, asin

def haversine(pos1, pos2):
  # pos type
  # {x:int, y:int}
  # x and y must be latitude and longitude

  # reference: https://en.wikipedia.org/wiki/Haversine_formula
  r = 6371 # jari2 bumi dalam km
  deg = pi/180
  dlat = (pos2["x"]-pos1["x"])*deg
  dlon = (pos2["y"]-pos1["y"])*deg
  akar = sin(dlat/2)**2 + cos(pos2["x"]*deg) * cos(pos1["x"]*deg) * sin(dlon/2)**2
  return 2*r*asin(sqrt(akar))

def tetangga(id, graph):
  ttg = []
  for i, adj in enumerate(graph[id]):
    if adj != 0:
      ttg.append(i)
  return ttg

def getdistancefrompath(path, parsed):
  out = []
  node = parsed[1]
  adj = parsed[3]
  distance = 0.0

  for i in range(len(path)-1):
    out.append((node.index(path[i]), node.index(path[i+1])))
  
  for edge in out:
    distance += adj[edge[0]][edge[1]]
  
  return distance

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
    ttg = {}
    for nodeid in tetangga(i, adj):
      distance = haversine(coor[nodeid], coor[i])
      ttg[node[nodeid]] = distance
      adj[i][nodeid] = distance
    listnode[node[i]] = ttg
  
  file.close()
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
