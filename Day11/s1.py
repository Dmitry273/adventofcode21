data = [[int(y) for y in x.strip()] for x in open('Day11/d11.txt', 'r')]

W = len(data)
H = len(data[0])

def neighbors(i, j):
    answ = []
    for x in range(max(0, i-1),min(W, i+2)):
        for y in range(max(0, j-1),min(H, j+2)):
            answ.append((x,y))
    answ.remove((i,j))
    return answ

def env_energy():
    for i in range(W):
        for j in range(H):
            data[i][j] += 1

answ = 0

def flashes():
    global answ
    c = 1
    while c:
        c = 0
        for i in range(W):
            for j in range(H):
                if data[i][j] > 9:
                    for neighbor in neighbors(i,j):
                        if data[neighbor[0]][neighbor[1]] != 0: data[neighbor[0]][neighbor[1]] += 1
                    data[i][j] = 0
                    answ += 1
                    c = 1
                
for step in range(100):
    env_energy()
    flashes()

print(answ)