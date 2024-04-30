answ = 0
data = []
for line in open('t1.txt', 'r'):
    data.append(int(line))

trip = sum(data[0:3])
for i in range(len(data)-3):
    new = trip + data[i+3] - data [i]
    if new > trip: answ += 1
    trip = new
print(answ)