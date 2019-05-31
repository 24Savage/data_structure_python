from typing import Dict

class GraphError(Exception):
    pass

class Graph:
    def __init__(self, dic: Dict[int,list]={}):
        self.__vnum = 0
        self.__table = {} # table以链接表的形式存储图，形如{0:[(vertex, weight)]}
        for v, e in dic.items():
            e.sort() # 默认出边列表元素的第一项是节点，第二项是权重
            self.__table[v] = list(e)
            self.__vnum += 1
            
    @property
    def v_num(self):
        return self.__vnum
        
    def is_empty(self):
        return self.__vnum == 0
        
    def get_vertex(self):   # 考虑到节点不一定是连续的数
        return [v for v in self.__table]
    
    def add_vertex(self, v:int):
        if self.__table.get(v):
            raise GraphError('vertex {0} already exist'%{v})
        self.__table[v] = []
        self.__vnum += 1
        
    def add_edge(self, vi:int, vj:int, val):
        assert 0 <= vi <self.__vnum
        edges = self.__table[vi]
        for i in range(len(edges)):
            if edges[i][0] > vj:
                edges.insert(i, (vj,val))
                return
            if edges[i][0] == vj:
                edges[i] = (vj,val)
                return 
        edges.insert(0, (vj,val))
        
        
    def out_edges(self, v:int):
        e = self.__table.get(v)
        if e is None:
            raise GraphError("Graph doesn\'t have vertex %s"%vi)
        return self.__table[v]
        
    def get_edge(self, vi:int, vj:int):
        e = self.__table.get(vi)
        lens = len(e)
        if e is None:
            raise GraphError("Graph doesn\'t have vertex %s"%vi)
        elif vj < 0 or vj > self.__vnum:
            raise GraphError("Graph doesn\'t have vertex %s"%vj)
        if vi == vj:
            return 0    # 节点到自己的距离为零
        l, r = 0, lens-1
        while l < r:    # 二分查找
            mid = (l + r)>>1
            if e[mid][0] >= vj:
                r = mid
            else:
                l = mid + 1
        if e[l][0] == vj:
            return e[l][1]
        return float('inf') # 不存在的边用无限大表示