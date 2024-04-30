pos = 0
dep = 0
for line in open('Day2/t2.txt', 'r'):
    if line.startswith('f'): pos += int(line[line.find(' '):])
    if line.startswith('u'): dep -= int(line[line.find(' '):])
    if line.startswith('d'): dep += int(line[line.find(' '):])
print(pos*dep)