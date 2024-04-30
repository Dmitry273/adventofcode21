a = float('inf')
answ = 0
for line in open('t1.txt', 'r'):
    if int(line) > a: answ += 1
    a = int(line)
print(answ)