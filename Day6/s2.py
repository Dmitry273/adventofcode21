data = [int(j) for j in [i.strip() for i in open('Day6/d6.txt','r')][0].split(',')]

types = [0]*9
print(types)
for fish in data:
    types[fish] += 1

for day in range(256):
    new = [0 for x in types]
    for type, total in enumerate(types):
        if type == 0:
            new[6] += total
            new[8] += total
        else:
            new[type-1] += total
    types = [x for x in new]

print(sum(types))