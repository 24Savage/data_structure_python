class Queue:
    '''
    采用环形表实现队列
    self.__elem为数据存储区域
    self.__len为目前数据存储区域的长度
    self.__num为已存取数据的数目
    self.__head头元素的位置'''
    def __init__(self,length=4):
        self.__elem=[None]*length
        self.__len=length
        self.__num=0
        self.__head=0
    def is_empty(self):
        return self.__num==0
    @property
    def peek(self):
        return self.__elem[self.__head]
    def dequeue(self):
        if self.__num==0:
            raise ValueError('dequeue from an empty Queue')
        e=self.__elem[self.__head]
        self.__head=(self.__head+1)%self.__len
        self.__num-=1
        return e
    def enqueue(self,val):
        print(self.__num)
        if self.__num==self.__len:
            self.__extend()
        self.__elem[(self.__head+self.__num)%self.__len]=val
        self.__num+=1
    def __extend(self):
        new_len=int(self.__len*1.125)
        new_elem=[None]*new_len
        for i in range(self.__len):
            new_elem[i]=self.__elem[(self.__head+i)%self.__len]
        self.__elem=new_elem
        self.__head=0
        self.__len=new_len

class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Queue_by_linkedlist():
    def __init__(self):
        self.tail=self.dummy=Node('dummy')
        self.num=0
    @property
    def is_empty(self):
        return self.num==0
    def enqueue(self,val):
        self.tail.next=Node(val)
        self.tail=self.tail.next
        self.num+=1
    def dequeue(self):
        if self.tail is None:
            raise ValueError('dequeue from empty queue')
        e=self.dummy.next.val
        self.dummy.next=self.dummy.next.next
        self.num-=1
        if self.num==0:
            self.tail=self.dummy
        return e
    @property
    def peek(self):
        return self.dummy.next.val