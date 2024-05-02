data = [i.strip() for i in open("Day5/t5.txt", "r")]

intersections = set()
clouds = set()
def process(cloud):
    if cloud in clouds:
        intersections.add(cloud)
    clouds.add(cloud)

for stream in data:    
    S = stream.replace(' -> ', ',')
    x1, y1, x2, y2 = [int(i) for i in S.split(',')]
    if x1 == x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            cloud = (x1, y)
            process(cloud)
    elif y1 == y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            cloud = (x, y1)
            process(cloud)
    else:
        if x1<x2 and y1<y2:
            for x, y in zip(range(x1, x2+1, 1), range(y1, y2+1, 1)):
                cloud = (x, y)
                process(cloud)
        if x1>x2 and y1<y2:
            for x, y in zip(range(x1, x2-1,-1), range(y1, y2+1, 1)):
                cloud = (x, y)
                process(cloud)
        if x1<x2 and y1>y2:
            for x, y in zip(range(x1, x2+1, 1), range(y1, y2-1,-1)):
                cloud = (x, y)
                process(cloud)
        if x1>x2 and y1>y2:
            for x, y in zip(range(x1, x2-1,-1), range(y1, y2-1,-1)):
                cloud = (x, y)
                process(cloud)
print(len(intersections))