from dec_prio_heap import DecPrioQueue
from graph import Graph, GraphError

def get_dis(G,v0):
    vnum = G.v_num
    seq = [(G.get_edge(v0,v), v0, v) for v in G.get_vertex()]
    queue = DecPrioQueue(seq)
    inf = float('inf')
    dis = {}
    while not queue.is_empty():
        W, vi ,vj = queue.dequeue()
        if W == inf:
            raise GraphError
        dis[vj] = ((vi,W))
        for v, w in G.out_edges(vj):
            if dis.get(v) is None and w+W < queue.weight(v):
                queue.dec_weight(w+W, vj, v)
    return dis
    
if __name__ == '__main__':
    e = {0:[(1,10),(2,9),(5,9)], 1:[(0,10),(3,6),(4,3)], 2:[(0,9),(3,10),(5,6),(6,8)], 3:[(1,6),(2,10),(6,4)], 4:[(1,3),(6,6)],\
5:[(0,9),(2,6),(6,7),(7,13)], 6:[(2,8),(3,4),(4,6),(5,7),(7,9),(8,10)], 7:[(5,13),(6,9),(8,8)], 8:[(6,10),(7,8)]}
    G = Graph(e)
    print(get_dis(G, 0))