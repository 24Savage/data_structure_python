import sys
sys.path.append(r'C:\Users\jiao\DataStructure\树')
from graph import Graph
from prio_queue import PrioQueue

def get_dis(G, v0):
    U = {}
    queue = PrioQueue([(0,v0,v0)]) # 初始化，表示此时在U集合里没有顶点， 最短的路径是从v0到v0
    while not queue.is_empty():
        W, vi, vj = queue.dequeue() # queue中存放U到V-U中的边，vi在U中，vj在V-U中
        if U.get(vj):   # 但有可能随着计算的进行，vj已经在在U中了
            continue
        U[vj] = (vi,W)  # U用来保存已经得到最短路径的节点v，vi是前一个节点，W是该路径的长度
        for v, w in G.out_edges(vj):
            if U.get(v):
                continue
            queue.enqueue((W+w,vj,v))
    return U

if __name__ == '__main__':
    e = {0:[(1,10),(2,9),(5,9)], 1:[(0,10),(3,6),(4,3)], 2:[(0,9),(3,10),(5,6),(6,8)], 3:[(1,6),(2,10),(6,4)], 4:[(1,3),(6,6)],\
5:[(0,9),(2,6),(6,7),(7,13)], 6:[(2,8),(3,4),(4,6),(5,7),(7,9),(8,10)], 7:[(5,13),(6,9),(8,8)], 8:[(6,10),(7,8)]}
    G = Graph(e)
    print(get_dis(G, 0))