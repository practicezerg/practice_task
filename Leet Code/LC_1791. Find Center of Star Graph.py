"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one
center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes
ui and vi. Return the center of the given star graph.
"""
def findCenter(edges):
    slov = {}
    for one_list in (edges):
        for num in one_list:
            if num in slov:
                slov[num] += 1
            else:
                slov[num] = 1
    print(slov)
    for i,v in slov.items():
        if v == len(edges):
            return i





edges = [[1,2],[5,1],[1,3],[1,4]]
res = findCenter(edges)
print(res)