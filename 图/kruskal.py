import sys
sys.path.append(r'C:\Users\jiao\DataStructure\树')
from graph import Graph
from prio_queue import PrioQueue

def get_mst(G):
    reps = {v:v for v in G.get_vertex()} # reps用于记录定点所在的连通分量
    mst = []
    pqueue = PrioQueue()
    for vi in reps:
        for vj, w in G.out_edges(vi):
            pqueue.enqueue((w,vi,vj)) # 把权重放在前面便于排序
    count = 0
    vnum = G.v_num
    while count < vnum and not pqueue.is_empty():
        w, vi, vj = pqueue.dequeue()
        if reps[vi] == reps[vj]:    # 得到权值最小且在不同联通分量的边
            continue
        mst.append(((vi,vj),w))
        orep, nrep = reps[vi], reps[vj]
        for v,r in reps.items():
            if r == orep:
                reps[v] = nrep    # 更新顶点所在的联通分量
    return mst # 如果count != vnum就表示没有找到最小生成树
        
    return mst
    
if __name__ == '__main__':
    e = {0:[(1,10),(2,9),(5,9)], 1:[(0,10),(3,6),(4,3)], 2:[(0,9),(3,10),(5,6),(6,8)], 3:[(1,6),(2,10),(6,4)], 4:[(1,3),(6,6)],\
5:[(0,9),(2,6),(6,7),(7,13)], 6:[(2,8),(3,4),(4,6),(5,7),(7,9),(8,10)], 7:[(5,13),(6,9),(8,8)], 8:[(6,10),(7,8)]}
    G = Graph(e)
    print(get_mst(G))