data = [int(j) for j in [i.strip() for i in open('Day6/t6.txt','r')][0].split(',')]

mydict = {}

testing = [8]
for day in range(88):
    for i in range(len(testing)):
        if testing[i] == 0:
            testing[i] = 6
            testing.append(8)
        else:
            testing[i] -= 1
    if day>=79:
        mydict.update({87-day:len(testing)})

answ = [mydict[i] for i in data]
print(sum(answ))