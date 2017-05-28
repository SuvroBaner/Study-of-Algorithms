### Eulerian Tour
# Input : A list of nodes
# Output: A list of tuples comprising of the Eulerian Path which results into a Tour

def create_Tour(nodes):
    tour = []
    node = 0
    firstNode = nodes[0]
    while node < len(nodes):
        if node < len(nodes)-1:
            tour.append((nodes[node], nodes[node+1]))
        else:
            tour.append((nodes[node], firstNode))
        node += 1
    return tour
    
def check_edge(t, b, nodes):
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes
    
def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree
    
def is_euclidean_tour(nodes, tour):
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print("Node %s has odd degrees"%node)
                return False
        except KeyError:
            print("Node %s is not present"%node)
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print("Your graph wasn't connected")
        return False

# Test whether it's an Eulerian Tour
# 1) All vertices have to be connected with atleast one other vertex, i.e. degree is atleast 1
# 2) All vertices must have an even degree of paths (edges)

def test():
    nodes = [1, 2, 3, 4]
    tour = create_Tour(nodes)
    return is_euclidean_tour(nodes, tour), tour

print(test())