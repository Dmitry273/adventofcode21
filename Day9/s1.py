
m = [[int(y) for y in x.strip()] for x in open('Day9/d9.txt', 'r')]

H = len(m)
W = len(m[0])

def neighbors(i, j):
    answ = []
    if i > 0 : answ.append([i-1,j])
    if i < H-1: answ.append([i+1,j])
    if j > 0 : answ.append([i,j-1])
    if j < W-1: answ.append([i,j+1])
    return answ

answ = 0

for i in range(H):
    for j in range(W):
        point = m[i][j]
        pool = []
        for adj in neighbors(i,j):
            pool.append(m[adj[0]][adj[1]])
        if point < min(pool): answ += 1+point

print(answ)