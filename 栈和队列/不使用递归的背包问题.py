import random
wlist = [random.randint(10,20) for _ in range(7)]
temp=[i for i in range(7)]
random.shuffle(temp)
weight=sum([wlist[i] for i in temp[:4]])

class Queue():
    def __init__(self,size=8):
        self.__elem=[None]*size
        self.__num=0
        self.__len=size
        self.__head=0
    def enqueue(self,val):
        if self.__num==self.__len:
            self.__expand()
        self.__elem[(self.__head+self.__num)%self.__len]=val
        self.__num+=1
    def __expand(self):
        new_elem=[None]*self.__len*2
        for i in range(self.__len):
            new_elem[i]=self.__elem[(self.__head+i)%self.__len]
        self.__elem=new_elem
        self.__len*=2
        self.__head=0
    def dequeue(self):
        if self.__num==0:
            raise ValueError('dequeue from an empty queue')
        e=self.__elem[self.__head]
        self.__head=(self.__head+1)%self.__len
        self.__num-=1
        return e
    @property
    def peek(self):
        return self.__elem[self.__head]
    @property
    def is_empty(self):
        return self.__num==0

def knap_st(weight, wlist):
    '''
    使用非递归(stack)的方式完成简单背包问题
    '''
    st = list()
    st.append((weight,0,1))    # (剩余容量，物品编号，是否选择该编号的物品)
    while st:
        cur, index, nxt= st.pop()
        if cur==0:
            while st:
                node=st.pop()
                if node[2]!=-1:
                    print('第%s个'%node[1],wlist[node[1]])
            return
        if index==len(wlist):
            continue
        for i in range(nxt,-1,-1):
            st.append((cur,index,i-1)) # 入栈在面对第index物品时的下一个选择
            st.append((cur-i*wlist[index],index+1,1))
            break
    print('Not found')
    
def knap_que(weight, wlist):
    '''
    使用非递归(queue)的方式完成简单背包问题
    '''
    q = Queue()
    q.enqueue((weight,0))
    dic=dict()
    while not q.is_empty:
        cur, index=q.dequeue()
        if cur==0:
            print('found')  # 结果怎么表达???
            return
        if index==len(wlist):
            continue
        for i in range(2):
            q.enqueue((cur-i*wlist[index],index+1))
    print('Not found')
    
print('weight:%s, wlist:%s'%(weight,wlist))
knap_que(weight, wlist)