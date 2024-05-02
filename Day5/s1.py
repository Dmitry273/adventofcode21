data = [i.strip() for i in open("Day5/d5.txt", "r")]

intersections = set()
clouds = set()

for stream in data:    
    S = stream.replace(' -> ', ',')
    x1, y1, x2, y2 = [int(i) for i in S.split(',')]
    if x1 == x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            cloud = (x1, y)
            if cloud in clouds:
                intersections.add(cloud)
            clouds.add(cloud)
    if y1 == y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            cloud = (x, y1)
            if cloud in clouds:
                intersections.add(cloud)
            clouds.add(cloud)
print(len(intersections))