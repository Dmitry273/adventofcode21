oxygen = []
co2 = []
data = [[int(j) for j in i.strip()] for i in open('Day3/t3.txt', 'r')]
W = len(data[0])
for pos in range(W):
    L = len(data)
    if L == 1:
        oxygen = [str(c) for c in data[0]]
        break
    new = [i for i in data if i[pos] == 1]
    C = '1'
    if len(new) < L-len(new):
        new = [i for i in data if i[pos] == 0]
        C = '0'
    data = new
    oxygen.append(C)

data = [[int(j) for j in i.strip()] for i in open('Day3/t3.txt', 'r')]
W = len(data[0])
for pos in range(W):
    L = len(data)
    if L == 1:
        co2 = [str(c) for c in data[0]]
        break
    new = [i for i in data if i[pos] == 0]
    C = '0'
    if len(new) > L-len(new):
        new = [i for i in data if i[pos] == 1]
        C = '1'
    data = new
    co2.append(C)

print(int(''.join(oxygen), 2))
print(int(''.join(co2), 2))
print(int(''.join(oxygen), 2)*int(''.join(co2), 2))