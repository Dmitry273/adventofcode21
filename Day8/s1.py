data = [i.strip() for i in open('Day8/d8.txt', 'r')]

answ = 0
for num in data:
    digits = num[num.find('|')+2:].split()
    print(digits)
    for digit in digits:
        if len(set(digit)) in [2,3,4,7]: answ += 1
print(answ)