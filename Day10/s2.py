from queue import LifoQueue

scores = {')':1,']':2,'}':3,'>':4}
pairs = {'(':')','[':']','{':'}','<':'>'}

data = [x.strip() for x in open('Day10/d10.txt', 'r')]

answ = []
for line in data:
    stack = LifoQueue()
    local_score = 0
    for char in line:
        if char in ['(','[','{','<']:
            stack.put(char)
        else:
            if pairs[stack.get()] != char:
                break
    else:
        while not stack.empty():
            local_score *= 5
            local_score += scores[pairs[stack.get()]]
    if local_score: answ.append(local_score)
        
answ.sort()     
print(answ[len(answ)//2])