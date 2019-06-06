from aov import get_topo
from graph import Graph, GraphError
from collections import defaultdict

def get_cri_paths(aov):
    def get_earliest_time(topo, aov):
        et = defaultdict(int)
        for i in topo:
            for j,w in aov.out_edges(i):
                if et[i] + w > et[j]:
                    et[j] = et[i] + w
        return et
    def get_latest_time(topo, aov, et_last):
        def inf():
            return float('inf')
        vnum = len(topo)
        lt = defaultdict(inf)
        lt[topo[-1]] = et_last
        for i in range(vnum-2, -1, -1):
            for j,w in aov.out_edges(topo[i]):
                print("{0}:{1},{2}".format(topo[i],j,w))
                if lt[j] - w < lt[topo[i]]:
                    lt[topo[i]] = lt[j] - w
        return lt
    topo = get_topo(aov)
    et = get_earliest_time(topo,aov)
    lt = get_latest_time(topo, aov, et[topo[-1]])
    print(et)
    print(lt)
    ans = []
    vnum = len(topo)
    for i in range(vnum):
        for j,w in aov.out_edges(topo[i]):
            if et[topo[i]] == lt[j] - w:
                ans.append((i,j))
    return ans
    
if __name__ == '__main__':
    e = {0:[(1,7),(2,13),(3,8)], 1:[(2,4),(5,14)], 2:[(4,5),(6,8),(7,12)], 3:[(4,13),(7,10)], \
    4:[(5,7),(6,3)], 5:[(8,5)], 6:[(8,7)], 7:[(8,8)], 8:[]}
    aov = Graph(e)
    print(get_cri_paths(aov))
