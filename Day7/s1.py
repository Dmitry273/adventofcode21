data = [int(j) for j in [i.strip() for i in open('Day7/d7.txt','r')][0].split(',')]

data.sort()
median = data[len(data)//2]

fuel = sum([abs(i-median) for i in data])

print(fuel)