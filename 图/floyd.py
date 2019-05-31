from graph import Graph

def get_mst(G):
    vnum = G.v_num
    inf = float('inf')
    A = [[0]*vnum for _ in range(vnum)]  # A[i][j]表示由i到j的、经过下标<=k节点的最小路径
    vertex = G.get_vertex()
    for vi in range(vnum):  # 初始化为由i到j的、不经过任何节点的最小路径
        for vj in range(vnum):
            A[vi][vj] = G.get_edge(vertex[vi],vertex[vj])
    N = [[None if A[vi][vj] == inf else vj for vj in range(vnum)] for vi in range(vnum)]    # N[i][j] 表示i到j的最短路径上，i的下一个节点
    for k in range(vnum):
        for vi in range(vnum):
            for vj in range(vnum):
                if A[vi][vj] > A[vi][k] + A[k][vj]:
                    A[vi][vj] = A[vi][k] + A[k][vj]
                    N[vi][vj] = N[vi][k]
    return (A, N)

if __name__ == '__main__':
    e = {0:[(1,10),(2,9),(5,9)], 1:[(0,10),(3,6),(4,3)], 2:[(0,9),(3,10),(5,6),(6,8)], 3:[(1,6),(2,10),(6,4)], 4:[(1,3),(6,6)],\
5:[(0,9),(2,6),(6,7),(7,13)], 6:[(2,8),(3,4),(4,6),(5,7),(7,9),(8,10)], 7:[(5,13),(6,9),(8,8)], 8:[(6,10),(7,8)]}
    G = Graph(e)
    print(get_mst(G)[1])