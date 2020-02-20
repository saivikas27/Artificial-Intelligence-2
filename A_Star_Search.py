
#import queue
import queue

#vertex list form of the given graph
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

#a_star search function
def a_star_search(graph, begin, dest):
    #visited vertex list
    visited= set()
    #expanded states list
    expanded=[]
    #priority queue as stack which chooses various paths depending on their a_star cost
    stack=queue.PriorityQueue(maxsize=0)
    stack.put((0,[begin]))
    while stack:
        cost,path = stack.get()
        node = path[-1]
        if node not in visited:
            #for the node not in visited vertex list and is about to expand add it to expanded list.
            expanded.append(node)
            cost = cost-graph[node]['hu']
            for i in graph[node]:
                # if i is not hu and is not yet visted then compute it for other steps
                if(i!='hu' and i not in visited):
                    sum = graph[i]['hu']
                    #calculation of the a_star cost
                    a_star_cost=cost+sum+graph[node][i]
                    alternate_path = list(path)
                    alternate_path.append(i)
                    stack.put((a_star_cost,alternate_path))
            #add the node expanded to the visited list
            visited.add(node)
        #if node is the destination then Goal is reached
        if node == dest:
            return path,expanded

shortest_path,expanded= a_star_search(graph, 'S', 'G')
#print the shortest path and expanded states
print("A_Star Search shortest path is =",shortest_path,"and expanded states are =",expanded)