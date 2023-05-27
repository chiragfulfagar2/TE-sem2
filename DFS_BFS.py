graph={
    '5': ['3','4'],
    '3':['2','6'],
    '4':['9'],
    '2':[],
    '6':[],
    '9':[],
}

visited_1=[]
queue=[]
visited_2=set()

def bfs(visited, graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("BFS is :")
bfs(visited_1,graph,'5')
print("\nDFS is : ")
dfs(visited_2,graph,'5')
