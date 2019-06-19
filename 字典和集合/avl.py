from binary_sort_tree import Node, Bst


class AvlNode(Node):
    def __init__(self,key, data):
        super(AvlNode,self).__init__(key,data)
        self.height = 0
        self.parent = None
        
    @property
    def bf(self):
        l = self.left.height if self.left else -1
        r = self.right.height if self.right else -1
        return l - r
        
    def update(self):  # 更新高度
        l, r = self.left, self.right
        if not l or not r:
            l = l if l else r
            if not l:
                self.height = 0
                return
            self.height = 1 + l.height
            return 
        self.height = max(l.height, r.height) + 1
        
    def set_left(self, other):
        self.left = other
        if other:
            other.parent = self
        
    def set_right(self, other):
        self.right = other
        if other:
            other.parent = self
        
    def __str__(self):
        return '{0}:{1},h:{2},bf:{3}'.format(self.key, self.data, self.height, self.bf)
        
class Dict(Bst):
    def set_root(self,node):
        self._root = node
        node.parent = None
    @staticmethod
    def LL(a):
        b = a.left
        a.set_left(b.right)
        b.set_right(a)
        a.update()
        b.update()
        return b
        
    @staticmethod
    def RR(a):
        b = a.right
        a.set_right(b.left)
        b.set_left(a)
        a.update()
        b.update()
        return b
        
    @staticmethod
    def LR(a):
        c = Dict.RR(a.left)
        a.set_left(c)
        return Dict.LL(a)
        
    @staticmethod
    def RL(a):
        c = Dict.LL(a.right)
        a.set_right(c)
        return Dict.RR(a)

    def __rebalance(self, node):
        while node:
            node.update()
            if abs(node.bf) > 1:
                self.balance(node)
            node = node.parent
        if not node:
            return
    def balance(self,node):
        bf = node.bf
        p = node.parent
        if bf == 2:
            if node.left.bf == 1:
                b = Dict.LL(node)
            else:
                b = Dict.LR(node)
        elif bf == -2:
            if node.right.bf == -1:
                b = Dict.RR(node)
            else:
                b = Dict.RL(node)
        if p is None:
            self.set_root(b)
            return
        if node.key < p.key:
            p.set_left(b)
        else:
            p.set_right(b)

    def insert(self,key,data):
        q = self._root    # q 是查找key所用的指针
        p = None
        node = AvlNode(key, data)
        if q is None:
            self._root = node
            return
        while q:
            if key < q.key:
                p, q = q, q.left
            elif key > q.key:
                p, q = q, q.right
            else:
                q.data = data
                return
        if key < p.key:
            p.set_left(node)
        else:
            p.set_right(node)
        self.__rebalance(p)
                
    def delete(self,key):
        p, q = None, self._root
        if q is None:
            return
        while q:
            if key < q.key:
                p, q = q, q.left
            elif key > q.key:
                p, q = q, q.right
            else:
                break
        if not q:
            raise KeyError
        l, r = q.left, q.right
        if not l or not r:
            l = l if l else r
            if not p:
                self.set_root(l)
                return
            if q is p.left:
                p.set_left(l)
            else:
                p.set_right(l)
            self.__rebalance(p)
            return
        p = q
        while l.right:
            p, l = l, l.right
        q.key, q.data = l.key, l.data
        if l is p.left:
            p.left = l.left
        else:
            p.right = l.left
        self.__rebalance(p)
        
if __name__ == '__main__':
    from random import randint
    D = Dict()
    arr = [4,1,10,0,2,7,13,3,6,8,12,14,5,9,11,15]
    for i in arr:
        D.insert(i,'x')
    print(D)
    D.print_tree()
    D.delete(4)
    print(D)
    D.print_tree()