from math import sqrt

def heuristics_distance(parsed, start_node, goal_node):
    for i in range(len(parsed[1])):
        # cari indeks simpul tujuan
        if parsed[1][i] == goal_node:
            end = i
    # Buat dictionary key = node, value = jarak lurus node ke simpul tujuan
    goal_dist = []
    h={}
    for i in range(len(parsed[1])):
        goal_dist.append(sqrt((parsed[2][i]["x"]-parsed[2][end]["x"])**2 + (parsed[2][i]["y"]-parsed[2][end]["y"])**2))
        h[parsed[1][i]] = goal_dist[i]
    return h


def sort_f (list, dictf):
    # Mengurutkan list simpul sesuai dengan F value terminimum
    dicttemp = {}
    for node in list:
        if dictf.get(node, "Not Available") != "Not Available":
          dicttemp[node] = dictf[node]
    dicttemp = dict(sorted(dicttemp.items(), key=lambda item: item[1]))
    sorted_list = []
    for i in dicttemp.keys():
      sorted_list.append(i)
    return sorted_list
      

# A* search
def astar_search(parsed, heuristics, start_node, goal_node): 
    
    # Inisialisasi open node dan closed node
    open_node = []
    closed_node = []

    # Bikin dictionary prev, key = node dan value = parent node
    prev = {}
    for i in parsed[1]:
      prev[i] = None

    # Bikin dictionary F value, G value
    dict_f= {}
    dict_f[start_node] = heuristics[start_node]

    dict_g = {}
    dict_g[start_node] = 0

    # Append simpul awal ke list open node
    open_node.append(start_node)
    
    # Looping open node hingga open node kosong
    while len(open_node) > 0:
        # Ambil simpul yang memiliki f value terkecil
        open_node = sort_f(open_node, dict_f)
        current_node = open_node.pop(0)
        closed_node.append(current_node)

        # Jika sudah mencapai simpul tujuan
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = prev[current_node]
            path.append(start_node)
            return path[::-1]

        # looping simpul tetangga dari current node
        neighbors = parsed[0][current_node]  

        for neighbor in neighbors.keys():    
            # Kasus simpul sudah diperiksa
            if(neighbor in closed_node):
                continue
            prev[neighbor] = current_node

            # Update nilai g value dan f value jika f value baru lebih minimum
            if(dict_g[current_node] + neighbors[neighbor] + heuristics[neighbor] < dict_f.get(neighbor, 99999999)):
              dict_g[neighbor] = dict_g[current_node] + neighbors[neighbor] 
              dict_f[neighbor] = dict_g[neighbor] + heuristics[neighbor]
              open_node.append(neighbor)
    # Return None jika tidak ada jalur
    return None