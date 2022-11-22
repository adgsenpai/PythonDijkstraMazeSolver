import numpy as np
import time
# make a matrix where 1 is a wall and 0 is a path and a * is the start and a + is the end
def makeMap(size):
    map = np.zeros((size,size))
    map[0,0] = 2
    map[size-1,size-1] = 3
    # make a random number of walls
    numWalls = np.random.randint(1,size)
    for i in range(numWalls):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        map[x,y] = 1        
    return map

def makeMapWithRecursiveDivision(size):
    map = np.zeros((size,size))
    map[0,0] = 2
    map[size-1,size-1] = 3
    #make a random number of walls
    numWalls = np.random.randint(1,size)
    for i in range(numWalls):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        map[x,y] = 1
    #make a random number of horizontal walls
    numWalls = np.random.randint(1,size)
    for i in range(numWalls):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        map[x,y] = 1
    #make a random number of vertical walls
    numWalls = np.random.randint(1,size)
    for i in range(numWalls):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        map[x,y] = 1
    #make a random number of diagonal walls
    numWalls = np.random.randint(1,size)
    for i in range(numWalls):
        x = np.random.randint(0,size)
        y = np.random.randint(0,size)
        map[x,y] = 1
    return map

 
def printMap(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i,j] == 1:
                print("#",end="")
            elif map[i,j] == 2:
                print("*",end="")
            elif map[i,j] == 3:
                print("+",end="")
            else:
                print(" ",end="")
        print()

def pathExists(map):
    #make sure that we can get from the start to the end
    #if we can, return True
    #if we can't, return False

    for i in range(len(map)):
        for j in range(len(map)):
            if map[i,j] == 2:
                start = (i,j)
            if map[i,j] == 3:
                end = (i,j)
    
    #make a list of all the places we have been
    been = []
    #make a list of all the places we need to go
    togo = [start]
    #while we still have places to go
    while len(togo) > 0:
        #get the next place to go
        place = togo.pop()
        #if we have been there, skip it
        if place in been:
            continue
        #if we are at the end, return True
        if place == end:
            return True
        #add the place to the list of places we have been
        been.append(place)
        #get the x and y coordinates of the place
        x,y = place
        #if we can go up, add it to the list of places to go
        if x > 0 and map[x-1,y] != 1:
            togo.append((x-1,y))
        #if we can go down, add it to the list of places to go
        if x < len(map)-1 and map[x+1,y] != 1:
            togo.append((x+1,y))
        #if we can go left, add it to the list of places to go
        if y > 0 and map[x,y-1] != 1:
            togo.append((x,y-1))
        #if we can go right, add it to the list of places to go
        if y < len(map)-1 and map[x,y+1] != 1:
            togo.append((x,y+1))
    #if we get here, we have no more places to go and we haven't found the end
    return False    
 
def Djikstra(map):
    # map is a matrix where 1 is a wall and 0 is a path and a * is the start and a + is the end
    # it is a numpy array

     #for each vertex v in Graph.Vertices:
     #     dist[v] ← INFINITY
     #     prev[v] ← UNDEFINED
     #     add v to Q
     #dist[source] ← 0

    for i in range(len(map)):
         for j in range(len(map)):
             if map[i,j] == 2:
                 start = (i,j)
             if map[i,j] == 3:
                 end = (i,j)
    dist = {}
    prev = {}
    Q = []
    for i in range(len(map)):
        for j in range(len(map)):
            dist[(i,j)] = np.inf
            prev[(i,j)] = None
            Q.append((i,j))
    dist[start] = 0
    while len(Q) > 0:
        #u ← vertex in Q with min dist[u]
        #remove u from Q
        u = min(Q,key=lambda x:dist[x])
        Q.remove(u)
        #for each neighbor v of u:
        #alt ← dist[u] + length(u, v)
        #if alt < dist[v]:
        #dist[v] ← alt
        #prev[v] ← u
        x,y = u
        if x > 0 and map[x-1,y] != 1:
            v = (x-1,y)
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
        if x < len(map)-1 and map[x+1,y] != 1:
            v = (x+1,y)
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
        if y > 0 and map[x,y-1] != 1:
            v = (x,y-1)
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
        if y < len(map)-1 and map[x,y+1] != 1:
            v = (x,y+1)
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist,prev


def printOptimalDjikstraPath(map):
    dist,prev = Djikstra(map)
    #S ← empty sequence
    #u ← target
    #if prev[u] is defined or u = source: 

    S = []
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i,j] == 3:
                u = (i,j)
    if prev[u] is not None or u == (0,0):
        #while u is defined: 
        #insert u at the beginning of S 
        #u ← prev[u] 
        while u is not None:
            S.insert(0,u)
            u = prev[u]
    #if S is empty:
    #return error (no path exists)
    if len(S) == 0:
        print("No path exists")
    #else:
    #return S (a path from source to target)
    else:
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i,j] == 1:
                    print("#",end="")
                elif map[i,j] == 2:
                    print("*",end="")
                elif map[i,j] == 3:
                    print("+",end="")
                elif (i,j) in S:
                    print("o",end="")
                else:
                    print(" ",end="")
            print()
  

start = time.time()

for i in range(100):    
    c= 1 
    try:
        map = makeMapWithRecursiveDivision(10)
        print("Map: {0}".format(i))                
        printMap(map)
        print("-------------------")
        print('Djikstra Path')
        try:
            printOptimalDjikstraPath(map)        
        except:
            print("Djikstra Failed due to unsolveable map")
        print()
        c += 1
    except:        
        pass
end = time.time()
print('Time to solve: {0}'.format(end-start))