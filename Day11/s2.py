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
    local = 0
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
                    local += 1
                    c = 1
    if local == 100: return 1
    else: return 0
                
for step in range(2000):
    env_energy()
    if flashes():
        print(step+1)
        break

#lmao? I though they'd ask something like "now, how about 100000000000 steps" or smth like that