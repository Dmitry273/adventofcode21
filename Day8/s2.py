data = [i.strip() for i in open('Day8/d8.txt', 'r')]

answ = 0
global_dict = {(0,1,2,4,5,6):'0',(2,5):'1',(0,2,3,4,6):'2',
               (0,2,3,5,6):'3',(1,2,3,5):'4',(0,1,3,5,6):'5',
               (0,1,3,4,5,6):'6',(0,2,5):'7',(0,1,2,3,4,5,6):'8',
               (0,1,2,3,5,6):'9'}
for ss in data:
    message = ss[ss.find('|')+2:].split()
    decode = ss[:ss.find('|')-1].split()
    segments = ['']*7
    full = ''.join(decode)
    freqs = {}
    # locate 2, 5 and 6 segment + construct dict with total number of occurrences for each char
    for char in ['a','b','c','d','e','f','g']:
        n = full.count(char)
        if n == 4: segments[4] = char
        if n == 9: segments[5] = char
        if n == 6: segments[1] = char
        freqs.update({char:n})
    # locate 3 segment
    for num in decode:
        if len(num) == 2:
            if freqs[num[0]] == 8: segments[2] = num[0]
            else: segments[2] = num[1]
    # locate 4 segment
    for num in decode:
        if len(num) == 4:
            for char in num:
                if freqs[char] == 7: segments[3] = char
    # locate 1 segment
    for num in decode:
        if len(num) == 3:
            for char in num:
                if freqs[char] == 8 and char not in segments: segments[0] = char
    # assign last segment
    for num in decode:
        if len(num) == 7:
            for char in num:
                if char not in segments: segments[6] = char
    information = []
    for num in message:
        code = []
        for char in num:
            code.append(segments.index(char))
        code.sort()
        information.append(global_dict[tuple(code)])
    answ += int(''.join(information))
    
print(answ)