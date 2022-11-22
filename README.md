# PythonDijkstraMazeSolver
given a matrix of [1s,0s] [*(start)] and [+(end)] computing the most optimal path in the matrix

Could be able to solve a matrix of size $M\times{N}$


![220px-Dijkstra_Animation](https://user-images.githubusercontent.com/45560312/203317022-8ce0315d-7ff6-414a-be55-6e34c6f03a59.gif)
![DijkstraDemo](https://user-images.githubusercontent.com/45560312/203316824-ed297a96-0fc0-4037-88a1-b69e059cab8c.gif)

**Standard truncated output**

```
Map: 94
*     #
  #  # #
  #  #
 #     #

         #
     #  #
      ##
    ##
         +
-------------------
Dijkstra Path
*ooo  #
  #o # #
  #o #
 # o   #
   o
   o     #
   o #  #
   o  ##
   o##
   oooooo+

Map: 95
* #    ###
    #   #
   #  #
  ##
 ##
  #
  ##
   #
     # #
  # ##   +
-------------------
Dijkstra Path
*o#oooo###
 ooo# oo#
   #  #ooo
  ##     o
 ##      o
  #      o
  ##     o
   #     o
     # # o
  # ##   +
```
#### Requirements you should get numpy thats it!

I used this Pseudocode provided by the wikipedia website to engineer my solution.

```
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
```

```
1  S ← empty sequence
2  u ← target
3  if prev[u] is defined or u = source:          // Do something only if the vertex is reachable
4      while u is defined:                       // Construct the shortest path with a stack S
5          insert u at the beginning of S        // Push the vertex onto the stack
6          u ← prev[u]                           // Traverse from target to source
```
