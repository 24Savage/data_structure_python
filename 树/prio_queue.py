from math import log

class PrioQueue:
    def __init__(self, seq=list()):
        self._elem = list(seq)
        self._size = len(self._elem)
        self._makeheap()
        
    def is_empty(self):
        return self._size == 0
        
    def enqueue(self,val):
        self._elem.append(val)
        self._shiftup(self._size)
        self._size += 1
    
    def _shiftup(self,start):
        elem= self._elem
        i = start
        j = (i-1)//2
        e = elem[i]
        while j > -1:
            if elem[j] <= e:
                break
            elem[i] = elem[j]
            i, j = j, (j-1)//2
        elem[i] = e
    
    def dequeue(self):
        if not self._size:
            raise IndexError('pop from empty prioQueue')
        elem = self._elem
        e0 = elem[0]
        e = elem.pop()
        self._size -= 1
        if self._size: # 只有一个元素时，无需进行向下交换
            elem[0] = e
            self._shiftdown(0)
        return e0
        
    def _shiftdown(self, start):
        elem = self._elem
        i, j = start, (start*2+1)
        end = self._size
        e = elem[i]
        while j < end:
            if j+1 < end and elem[j+1] < elem[j]:
                j += 1
            if elem[j] >= e:
                break
            elem[i] = elem[j]
            i, j = j, 2*j+1
        elem[i] = e
        
    def _makeheap(self):
        elem = self._elem
        length = self._size
        for i in range(length//2-1, -1, -1):
            self._shiftdown(i)
            
    def show(self):
        h = log(self._size, 2)//1
        h = int(h)
        elem = self._elem
        print(elem[:1])
        for i in range(1, h):
            print(elem[2**i-1 : 2**(i+1)-1])
        print(elem[2**h-1 :], '\n', '-'*self._size)