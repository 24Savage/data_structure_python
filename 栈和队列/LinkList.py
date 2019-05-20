class Node():
    def __init__(self,val):
        self.val=val
        self.next_=None

class LinkList():
    # 实现将可迭代对象转换为链表
    def __init__(self,seq=None):
        if seq is None:
            self.dummy=Node('dummy')
            self.pre_tail=None
            self.length=0
        else:
            self.length=0
            self.dummy=Node('dummy')
            cur=self.dummy
            for i in seq:
                cur.next_=Node(i)
                cur=cur.next_
                self.length+=1
            self.tail=cur
    def is_empty(self):
        return self.dummy.next_ is None
    def __len__(self):
        return self.length
    def __elements__(self):
        cur=self.dummy
        while cur.next_:
            yield (cur.next_.val)
            cur=cur.next_
    # 在最后加入节点,O(1)
    def add(self,val):
        if self.tail is None:
            self.tail=Node(val)
            self.dummy.next_=self.tail
            self.length+=1
        else:
            self.tail.next_=Node(val)
            self.tail=self.tail.next_
            self.length+=1
    # 在index位置掺入元素
    def insert(self,index,val):
        if index>self.length:
            raise IndexError('index out of range')
        i=0
        pre = self.dummy
        cur=self.dummy.next_
        while i<index:
            i+=1
            pre=pre.next_
            cur=cur.next_
        new_node=Node(val)
        new_node.next_=cur
        pre.next_=new_node
        self.length+=1
    # pop index位置的节点，O(n)，如何改为pop末尾元素复杂度O(1)
    def pop(self,index):
        if type(index) is not int:
            raise TypeError('interger argument expect got %s'%type(index))
        if not self.length:
            raise IndexError('pop from an empty list')
        if index < 0:
            index=self.length+index
        if index>=self.length:
            raise IndexError('index out of range')
        i=0
        pre = self.dummy
        cur=self.dummy.next_
        while i<index:
            pre=pre.next_
            cur=cur.next_
            i+=1
        r=cur.val
        pre.next_=cur.next_
        self.length-=1
        return r
    @staticmethod
    def merge(l1,l2):
        fake_node = Node('trump')
        tail = fake_node
        while l1 and l2:
            # 因为结果要求从左向右依次减小，因此始终把变量l1指向val小的节点
            # tail相当于一个针的作用
            if l1.val > l2.val:
                l1,l2=l2,l1
            tail.next_=l1
            l1=l1.next_
            tail=tail.next_
        if l1:
            tail.next_=l1
        if l2:
            tail.next_=l2
        return fake_node.next_
    # merger_sort
    @staticmethod
    def merge_sort(head):
        if not head or not head.next_:
            return head
        # 利用快慢指针，找到mid，fast走两步，slow走一步
        slow,fast=head,head.next_
        while fast and fast.next_:
            fast=fast.next_.next_
            slow=slow.next_
        mid=slow.next_
        # 断开连接
        slow.next_=None
        return LinkList.merge(LinkList.merge_sort(head), LinkList.merge_sort(mid))
    def sort(self):
        # 排序完成后，dummy和tail的引用指向要更正
        self.dummy.next_=LinkList.merge_sort(self.dummy.next_)
        while self.tail.next_:
            self.tail = self.tail.next_
    # 插入排序
    def insert_sort_v0(self):
        cur=self.dummy.next_
        if not cur or not cur.next_:
            return 
        crt=cur.next_
        # 断开有序部分和乱序部分的连接，以便写出cur的遍历终止条件
        cur.next_=None
        while crt:
            cur=self.dummy.next_
            pre=self.dummy
            while cur and cur.val<crt.val:
                pre=pre.next_
                cur=cur.next_
            next_crt=crt.next_
            crt.next_=pre.next_
            pre.next_=crt
            crt=next_crt
        # 更新尾部引用域
        if not cur:
            self.tail=pre.next_
        else:
            while cur.next_:
                cur=cur.next_
            self.tail=cur
    # dont need to redirect self.tail, this method just change Node's val
    # 貌似也很慢
    def insert_sort_v1(self):
        if not self.dummy.next_ or not self.dummy.next_.next_:
            return
        crt=self.dummy.next_.next_
        while crt:
            x=crt.val
            cur=self.dummy.next_
            while cur is not crt and cur.val<=x:
                cur=cur.next_
            while cur is not crt:
                y=cur.val
                cur.val=x
                x=y
                cur=cur.next_
            cur.val=x
            crt=crt.next_

if __name__ == '__main__':
    from random import randint
    r=LinkList([randint(0,10) for _ in range(7)])
    print(list(r.__elements__())))
    r.insert_sort_v1()
    print(list(r.__elements__()))
    print(r.tail.val)