data = [int(j) for j in [i.strip() for i in open('Day7/d7.txt','r')][0].split(',')]

mean = sum(data)/len(data)
dev = sum([(i-mean)/abs(i-mean) for i in data])/(2*len(data))

target = round(mean + dev)
print(mean, dev, target)

def fuel_cons(pos, target):
    delta = pos - target
    return (delta**2 + abs(delta))//2

answ = sum([fuel_cons(i, target) for i in data])
check1 = sum([fuel_cons(i, target-1) for i in data])
check2 = sum([fuel_cons(i, target+1) for i in data])
if check1 < answ or check2 < answ: print('hol up')
print(answ)
