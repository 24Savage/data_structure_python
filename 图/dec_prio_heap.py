'''在prim算法中，优先队列里记录了很多不必要的边，改进空间复杂度的方法如下：
每次向U中加入顶点，可能会遇到由U到V-U的更短的边，更新之，因此叫可减权堆
可减权堆里始终维护着U到V-U中的顶点的最短边
这样做，空间复杂度可以降为O（V）
'''
from sys import path
path.append(r'C:\Users\jiao\DataStructure\树')
from prio_queue import PrioQueue
from graph import Graph, GraphError

class DecPrioQueue(PrioQueue):
    def __init__(self, seq):
        self._elem = list(seq)  # List[(w,vi,vj)]
        self._size = len(self._elem)
        self._index = [i for i in range(self._size)] # _index中记录着vj和(w,vi,vj)在_elem中的索引的对应关系
        self._makeheap()
    
    def _shiftup(self,start):
        elem= self._elem
        index = self._index
        i = start
        j = (i-1)//2
        e = elem[i]
        while j > -1:
            if elem[j] <= e:
                break
            elem[i] = elem[j]
            index[elem[i][2]] = i
            i, j = j, (j-1)//2
        elem[i] = e
        index[e[2]] = i
    
    def dequeue(self):
        if not self._size:
            raise IndexError('pop from empty prioQueue')
        elem = self._elem
        index = self._index
        e0 = elem[0]
        index[e0[2]] = -1 # 将要弹出的顶点对应值标记为-1，表示该点不在V-U中，其实标不标记无所谓，后面再也不会检索它
        e = elem.pop()
        self._size -= 1
        if self._size:
            elem[0] = e
            self._shiftdown(0)
        return e0
        
    def _shiftdown(self, start):
        elem = self._elem
        index = self._index
        i, j = start, (start*2+1)
        end = self._size
        e = elem[i]
        while j < end:
            if j+1 < end and elem[j+1] < elem[j]:
                j += 1
            if elem[j] >= e:
                break
            elem[i] = elem[j]
            index[elem[i][2]] = i
            i, j = j, 2*j+1
        elem[i] = e
        index[e[2]] = i
    
    def weight(self,vj):
        '''以堆元素的第三个值为索引，找到index，并返回权值，复杂度O(1)'''
        ind = self._index[vj]
        return self._elem[ind][0]
        
    def dec_weight(self,w,vi,vj):
        '''寻找出第三个元素为vj的堆元素，并修改之为(w,v,vj)
        时间复杂度为log(n)'''
        ind = self._index[vj]
        self._elem[ind] = (w,vi,vj)
        self._shiftup(ind)
        
def get_mst(G):
    vnum = G.v_num
    mst = {}
    inf = float('inf')
    seq = [(G.get_edge(0,v), 0, v) for v in G.get_vertex()]
    queue = DecPrioQueue(seq)
    while not queue.is_empty():
        w, vi, vj = queue.dequeue()
        if w == inf:    # U到V-U不存在最小的边，说明整个图没有生成树
            raise GraphError
        mst[vj] = ((vi,vj),w)
        for v,w in G.out_edges(vj):
            if mst.get(v) is None and w < queue.weight(v):  # 发现了到顶点v的更小的边
                queue.dec_weight(w,vj,v)
    return mst

if __name__ == '__main__':
    e = {0:[(1,1),(4,3),(3,4)], 1:[(3,4),(4,2)], 2:[(4,4),(5,5)], \
    3:[(0,4),(1,4),(4,4)], 4:[(0,3),(1,2),(2,4)], 5:[(2,5),(4,7)]}
    G = Graph(e)
    print(get_mst(G))