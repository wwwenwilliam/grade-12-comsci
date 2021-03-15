

def dfs(current):
    global visited, adjHouses
    visited[current-1] = True
    for house in adjHouses[current]:
        if not visited[house-1]:
            dfs(house)

inData = input().split()

numHouses = int(inData[0])
numRoads = int(inData[1])
houseA = int(inData[2])
houseB = int(inData[3])
adjHouses = {}

for i in range(numHouses):
    adjHouses[i+1] = []
    
for i in range(numRoads):
    road = input().split()
    roadOne = int(road[0])
    roadTwo = int(road[1])
    adjHouses[roadOne].append(roadTwo)
    adjHouses[roadTwo].append(roadOne)
    
visited = [False for i in range(numHouses)]

dfs(houseA)

if visited[houseB-1]:
    print("GO ALBERT")
else:
    print("NO ALBERT")