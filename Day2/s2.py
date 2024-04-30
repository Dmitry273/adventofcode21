pos = 0
dep = 0
aim = 0
for line in open('Day2/t2.txt', 'r'):
    if line.startswith('f'): 
        pos += int(line[line.find(' '):])
        dep += aim*int(line[line.find(' '):])
    if line.startswith('u'): aim -= int(line[line.find(' '):])
    if line.startswith('d'): aim += int(line[line.find(' '):])
print(pos*dep)