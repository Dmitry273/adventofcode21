data = [i.strip() for i in open('Day3/t3.txt', 'r')]
freqs = [0]*len(data[0])

def adder(a, b):
    answ = []
    for i, j in zip(a,b):
        answ.append(i+j)
    return answ

for line in data:
    freqs = adder(freqs, [int(i) for i in line])

gamma = []
epsilon = []
for i in freqs:
    if i > 500:
        gamma.append('1')
        epsilon.append('0')
    if i < 500:
        gamma.append('0')
        epsilon.append('1')
    if i == 500: print('oh no')

print(int(''.join(gamma), 2)*int(''.join(epsilon), 2))
