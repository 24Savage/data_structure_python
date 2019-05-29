import sys
sys.path.append(r'C:\Users\jiao\DataStructure\树')
from graph import Graph
from prio_queue import PrioQueue

def get_mst(G):
    vnum = G.v_num
    count = 0
    mst = {}
    queue = PrioQueue([(0,None,0)])  # 优先队列用来存放从U到V-U的边，(w,vi,vj) 表示从vi到vj的权为w的边
    while count < vnum and not queue.is_empty():
        w, vi, vj = queue.dequeue()
        if mst.get(vj):
            continue
        count += 1
        mst[vj] = ((vi,vj),w)   # 表示在最小生成树中，vj的上一个顶点是vi
        for vk, w in G.out_edges(vj):
            if mst.get(vk) is None:
                queue.enqueue((w,vj,vk))
    return [e for v,e in mst.items()]
    
if __name__ == '__main__':
    e = {0:[(1,10),(2,9),(5,9)], 1:[(0,10),(3,6),(4,3)], 2:[(0,9),(3,10),(5,6),(6,8)], 3:[(1,6),(2,10),(6,4)], 4:[(1,3),(6,6)],\
5:[(0,9),(2,6),(6,7),(7,13)], 6:[(2,8),(3,4),(4,6),(5,7),(7,9),(8,10)], 7:[(5,13),(6,9),(8,8)], 8:[(6,10),(7,8)]}
    G = Graph(e)
    print(get_mst(G))