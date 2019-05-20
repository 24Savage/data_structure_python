class Btree():
    '''
    Binary tree based on <class 'list'>
    '''
    def __init__(self, root, L=None, R=None):
        assert isinstance(L, Btree) or L is None
        assert isinstance(R, Btree) or R is None
        self.__root = root
        self.__left = L
        self.__right = R
        self.__size = self.__getsize()
        
    def __getsize(self):
        s = 1
        for i in (self.__left, self.__right):
            if isinstance(i, Btree):
                s += i.size
        return s
        
    def is_empty(self):
        return self.__root is None
        
    def __str__(self):
        if not self.__right:
            if not self.__left:
                return "[{0}]".format(self.__root)
            return "[{0} {1}]".format(self.__root, self.__left)
        return "[{0} {1} {2}]".format(self.__root, self.__left, self.__right)
    
    @property
    def size(self): # return number of nodes
        return self.__size
    
    @property
    def root(self):
        return self.__root
        
    @property
    def left(self):
        return self.__left
        
    @property
    def right(self):
        return self.__right
    
    def set_root(val):
        assert isinstance(val, (int,float,complex))
        self.__root = val
    
    def set_left(self, t):
        assert isinstance(t, Btree) or t is None
        self.__left = t
    
    def set_right(self, t):
        assert isinstance(t, Btree) or t is None
        self.__right = t
        
if __name__ == '__main__':
    F = Btree('F')
    G = Btree('G')
    D = Btree('D', F, G)
    I = Btree('I')
    H = Btree('H')
    E = Btree('E', I, H)
    C = Btree('C', D, E)
    K = Btree('K')
    L = Btree('L')
    J = Btree('J', K, L)
    H.set_right(J)
    print(C)
