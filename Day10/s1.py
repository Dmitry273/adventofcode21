from queue import LifoQueue

scores = {')':3,']':57,'}':1197,'>':25137}
pairs = {'(':')','[':']','{':'}','<':'>'}

data = [x.strip() for x in open('Day10/d10.txt', 'r')]

answ = 0
for line in data:
    stack = LifoQueue()
    for char in line:
        if char in ['(','[','{','<']:
            stack.put(char)
        else:
            if pairs[stack.get()] != char:
                answ += scores[char]
                break
print(answ)