class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return '{0}:{1}'.format(self.key, self.data)

class Bst:
    '''利用二叉搜索树实现字典'''
    def __init__(self):
        self._root = None
        
    def __str__(self):
        node = self._root
        if node is None:
            return ''
        ans = []
        st = []
        while node or st:
            while node:
                st.append(node)
                node = node.left
            node = st.pop()
            ans.append(str(node))
            node = node.right
        return str(ans)
        
    def print_tree(self):
        root = self._root
        if not root:
            return
        queue = [root]
        bfs = []
        while True:
            bfs.append(['%2d'%(node.key) if node else None for node in queue])
            all_None = True
            for _ in range(len(queue)):
                r = queue.pop(0)
                if r:
                    all_None = False
                    queue.append(r.left)
                    queue.append(r.right)
                else:
                    queue.append(None)
                    queue.append(None)
            if all_None:
                bfs.pop()
                break
        h = len(bfs)
        ans = [['__']*(len(bfs[-1])*2-1) for _ in range(h)]
        for i in range(h):
            s = 2**(h-i-1)-1
            for v in bfs[i]:
                if v is not None:
                    ans[i][s] = str(v)
                s += 2**(h-i)
        for cor in ans:
            print(' '.join(cor))
        print('--'*(len(bfs[-1])*2))
        
    def insert(self, key,data):
        root = self._root
        if root is None:
            self._root = Node(key,data)
            return
        while True:
            if root.key > key:
                if root.left is None:
                    root.left = Node(key,data)
                    return
                root = root.left
            elif root.key < key:
                if root.right is None:
                    root.right = Node(key,data)
                root = root.right
            else:
                return
                
    def delete(self, key):
        p, c = None, self._root
        if c is None:
            return 
        while c:
            if key < c.key:
                p, c = c, c.left
            elif key > c.key:
                p, c = c, c.right
            else:
                break
        if c is None:
            raise KeyError
        l, r = c.left, c.right
        if not l or not r:
            l = l if l else r   # avoid write too many if else
            if not p:
                self._root = l
                return
            if c is p.left:
                p.left = l
            else:
                p.right = l
            return
        p = c
        while l.right:
            p, l = l, l.right
        c.key, c.data = l.key, l.data
        if p.left is l:
            p.left = l.left
        else:
            p.right = l.right
                
                
if __name__ == '__main__':
    from random import randint
    b = Bst()
    for i in [15,14,13,12]:
        b.insert(i,'*')
    print(b)
    b.print_tree()
    b.delete(15)
    print(b)
    b.print_tree()