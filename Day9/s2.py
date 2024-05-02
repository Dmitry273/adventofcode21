from queue import Queue

m = [[int(y) for y in x.strip()] for x in open('Day9/d9.txt', 'r')]

H = len(m)
W = len(m[0])

def neighbors(i, j):
    answ = []
    if i > 0 : answ.append((i-1,j))
    if i < H-1: answ.append((i+1,j))
    if j > 0 : answ.append((i,j-1))
    if j < W-1: answ.append((i,j+1))
    return answ

lows = []

for i in range(H):
    for j in range(W):
        point = m[i][j]
        pool = []
        for adj in neighbors(i,j):
            pool.append(m[adj[0]][adj[1]])
        if point < min(pool): lows.append((i,j))

basins = []

for low in lows:
    new_basin = set([low])
    front = Queue()
    front.put(low)
    while not front.empty():
        next = front.get()
        group_of_neighbors = neighbors(*next)
        for neighbor in group_of_neighbors:
            if neighbor not in new_basin and m[neighbor[0]][neighbor[1]] != 9:
                new_basin.add(neighbor)
                front.put(neighbor)
                if neighbor in lows:
                    lows.remove(neighbor)
                    print('got one')
    basins.append(len(new_basin))

basins.sort(reverse= True)
print(basins[0]*basins[1]*basins[2])

