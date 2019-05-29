from typing import Dict

class GraphError(Exception):
    pass

class Graph:
    def __init__(self, dic: Dict[int,list]={}, unconn=0):
        self.__vnum = 0
        self.__table = {} # table以链接表的形式存储图，形如{0:[vertex, weight]}
        self.unconn = unconn
        for v, e in dic.items():
            e.sort()
            self.__table[v] = e
            self.__vnum += 1
            
    @property
    def v_num(self):
        return self.__vnum
        
    def is_empty(self):
        return self.__vnum == 0
        
    def get_vertex(self):
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
        return self.__table.get(v)
        
    def get_edges(self, vi:int, vj:int):
        e = self.__table.get(vi)
        if e is None or vj<0 or vj>len(e):
            raise GraphError("Graph doesn\'t have vertex %s"%vi)
        return e[vj]