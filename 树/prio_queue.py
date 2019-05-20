from math import log

class PrioQueue:
    def __init__(self, seq=list()):
        self.__elem = list(seq)
        self.__size = len(self.__elem)
        self.__makeheap()
        
    def enqueue(self,val):
        self.__elem.append(val)
        self.__size += 1
        self.__shiftup()
    
    def __shiftup(self):
        elem= self.__elem
        i = len(elem)-1
        j = (i-1)//2
        e = elem[-1]
        while j > -1:
            if elem[j] <= e:
                break
            elem[i] = elem[j]
            i, j = j, (j-1)//2
        elem[i] = e
    
    def dequeue(self):
        if not self.__size:
            raise IndexError('pop from empty prioQueue')
        e0 = self.__elem[0]
        self.__elem[0] = self.__elem.pop()
        self.__size -= 1
        if self.__size:
            self.__shiftdown(0)
        return e0
        
    def __shiftdown(self, start):
        elem = self.__elem
        i, j = start, (start*2+1)
        end = self.__size
        e = elem[0]
        while j < end:
            if j+1 < end and elem[j+1] < elem[j]:
                j += 1
            if elem[j] >= e:
                break
            elem[i] = elem[j]
            i, j = j, 2*j+1
        elem[i] = e
        
    def __makeheap(self):
        elem = self.__elem
        length = self.__size
        for i in range(length//2-1, -1, -1):
            self.__shiftdown(i)
            
    def show(self):
        h = log(self.__size, 2)//1
        h = int(h)
        elem = self.__elem
        print(elem[:1])
        for i in range(1, h):
            print(elem[2**i-1 : 2**(i+1)-1])
        print(elem[2**h-1 :], '\n', '-'*self.__size)