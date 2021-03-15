def bfs():
    if len(queue) == 0:
        return

    current = queue.pop(0)
    for house in adjHouses[current]:
        if not visited[house-1]:
            visited[house-1] = True
            distMap[house] = [distMap[current][0]+1, current]
            queue.append(house)
    bfs()




inData = input().split()

numHouses = int(inData[0])
numRoads = int(inData[1])
houseA = int(inData[2])
houseB = int(inData[3])
adjHouses = {}
distMap = {}

for i in range(numHouses):
    adjHouses[i+1] = []
    distMap[i+1] = []
    
for i in range(numRoads):
    road = input().split()
    roadOne = int(road[0])
    roadTwo = int(road[1])
    adjHouses[roadOne].append(roadTwo)
    adjHouses[roadTwo].append(roadOne)
    
queue = [houseA]
visited = [False for i in range(numHouses)]
visited[houseA-1] = True
distMap[houseA] = [0, 0]

bfs()


if visited[houseB-1]:
    path = [houseB]
    while path[-1] != 0:
        path.append(distMap[path[-1]][1])
    path.pop()
    print("GO ALBERT")
    print(path)
else:
    print("NO ALBERT")