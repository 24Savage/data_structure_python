class Btree():
    '''
    Binary tree based on <class 'list'>
    '''
    def __init__(self, root, L=None, R=None):
        assert isinstance(root, (int,float,complex,str))
        assert isinstance(L, Btree) or L is None
        assert isinstance(R, Btree) or R is None
        self.__root = root
        self.__left = L
        self.__right = R
        
    def count_nodes(self):
        '''返回叶子节点和非叶子节点的数量'''
        if not self.__left and not self.__right:
            return (0, 1)
        leaf, non_leaf = 0, 1
        for i in (self.__left, self.__right):
            if isinstance(i, Btree):
                res = i.count_nodes()
                non_leaf += res[0]
                leaf += res[1]
        return (non_leaf, leaf)
        
    @property
    def depth(self):
        ld = self.__left.depth if self.__left else 0
        rd = self.__right.depth if self.__right else 0
        return 1 + max(ld, rd)
        
    def is_empty(self):
        return self.__root is None
        
    def __str__(self):
        if not self.__right:
            if not self.__left:
                return "[{0}]".format(self.__root)
            return "[{0} {1}]".format(self.__root, self.__left)
        return "[{0} {1} {2}]".format(self.__root, self.__left, self.__right)
        
    def __get_coordinates(self):
        root = self
        queue = [root]
        ans = list()
        while queue:
            n = len(queue)
            flag = 1
            temp = list()
            for _ in range(n):
                root = queue.pop(0)
                if root:
                    flag = 0
                    queue.append(root.left)
                    queue.append(root.right)
                    temp.append(root.val)
                else:
                    temp.append(None)
                    queue.append(None)
                    queue.append(None)
            if flag == 1:
                break
            ans.append(temp[:])
        width = len(ans[-1])*2 - 1
        height = len(ans)
        cors = list()
        for y in range(height-1,-1,-1):
            x = 2**y - 1
            step = 2**(y+1)
            for elem in ans[height-1-y]:
                if elem is not None:
                    cors.append((x,y,elem))
                x += step
        return (width, cors)
                
    def show(self):
        '''
        可视化展示当前二叉树
        下一步计划：添加节点间的连线'''
        import turtle
        width, cors = self.__get_coordinates()
        turtle.setworldcoordinates(-0.5,-0.5,width,width//2)
        turtle.hideturtle()
        turtle.penup()
        turtle.tracer(0)
        for cor in cors:
            x, y, elem = cor
            turtle.goto(x, y)
            turtle.pendown()
            turtle.write(elem, font=("Arial", 12, "normal"))
            turtle.penup()
        turtle.Screen().exitonclick()
        
    def left_right_root(self):
        root = self
        st = list()
        traversals = list()
        while st or root:
            while root:
                st.append(root)
                root = root.left if root.left else root.right
            # print([elem.val for elem in st])
            root = st.pop()
            traversals.append(root.val)
            if st and st[-1].left is root:
                root = st[-1].right
            else:
                root = None
        return traversals
        
    def root_left_right(self):
        root = self
        st = list()
        traversals = list()
        while root or st:
            while root:
                if root.right:
                    st.append(root.right)
                traversals.append(root.val)
                root = root.left
            if st:
                root = st.pop()
        return traversals
        
    def left_root_right(self):
        root = self
        st = list()
        traversals = list()
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            traversals.append(root.val)
            root = root.right
        return traversals
    
    @property
    def val(self):
        return self.__root
        
    @property
    def left(self):
        return self.__left
        
    @property
    def right(self):
        return self.__right
    
    def set_root(val):
        assert isinstance(val, (int,float,complex,str))
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
    C.show()
