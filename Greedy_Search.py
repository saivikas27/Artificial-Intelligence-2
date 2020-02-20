#import the queue
import queue
#the given graph is taken as a vertex-list
#hu is the heuristic of the corresponding vertex
graph={'S':{'hu':0,'d':3,'e':9,'p':1},
       'a':{'b':2,'c':2,'hu':5 },
       'b':{'a':2,'d':1,'hu':7},
       'c':{'a':2,'d':8,'f':3,'hu':4},
       'd':{'b':1,'c':8,'e':2,'S':3,'hu':7},
       'e':{'d':2,'S':9,'h':8,'r':2,'hu':5},
       'f':{'c':3,'G':2,'r':2,'hu':2},
       'G':{'f':2,'hu':0},
       'h':{'e':8,'p':4,'q':4,'hu':11},
       'p':{'h':4,'q':15,'S':1,'hu':14},
       'q':{'h':4,'p':15,'hu':12},
       'r':{'e':2,'f':2,'hu':3},
}
#the function which returns states expanded an the shortest path
def greedy_search(graph, begin, dest):
    #the set to store visited vertices
    visited= set()
    #the expanded vertices list
    expanded=[]
    #priority queue as stack for computation
    stack=queue.PriorityQueue(maxsize=0)
    stack.put((0,[begin]))
    #if the queue is not empty
    while stack:
        cost,path = stack.get()
        node = path[-1]
        #if node not in visited vertex list then expand it
        if node not in visited:
            expanded.append(node)
            #for all the neighbouring vertices of the node
            for i in graph[node]:
                if(i!='hu' and i not in visited):
                    #The cost is the hueristic cost of the current node
                    cost = graph[i]['hu']
                    #creating alternate path using the single paths
                    alternate_path = list(path)
                    alternate_path.append(i)
                    #add all the paths to the priority queue
                    stack.put((cost,alternate_path))
            visited.add(node)
        #if node is the destination then the Goal state is reached
        if node == dest:
            #return the shortest path and list of expanded states
            return path,expanded

shortest_path,expanded= greedy_search(graph, 'S', 'G')
#print the output
print("Greedy search shortest path is =",shortest_path,"and expanded states are =",expanded)