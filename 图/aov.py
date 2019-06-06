from graph import Graph, GraphError
from collections import defaultdict

def get_topo(aov):
    vertex = aov.get_vertex()
    vnum = aov.v_num
    rec = defaultdict(int)
    for vi in vertex:
        for vj, w in aov.out_edges(vi):
            rec[vj] += 1
    top = -1
    for v in vertex:
        if rec[v] == 0:
            rec[v] = top
            top = v
    ans = []
    while top != -1:
        ans.append(top)
        temp = rec[top]
        for v, w in aov.out_edges(top):
            rec[v] -= 1
            if rec[v] == 0:
                rec[v] = temp
                temp = v
        top = temp
    if len(ans) != vnum:
        raise GraphError('parameter not a AOV network')
    return ans

if __name__ == '__main__':
    e = {1:[(5,1),(3,1),(4,2)], 2:[(3,1),(6,1)], 3:[(7,1),(9,1),(8,1)], 4:[(7,1),(8,1),(10,1)], \
    5:[(7,1)], 6:[(8,1)], 7:[(9,1),(10,1)], 8:[(9,1),(10,1)], 9:[], 10:[]}
    aov = Graph(e)
    print(get_topo(aov))