graph ={
    '5':['8','6'],
    '8':['1','2'],
    '6':['3','4'],
    '1':[],
    '2':[],
    '3':[],
    '4':[], 
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="  ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("following is the breadth first  search")
bfs(visited,graph,'5')
