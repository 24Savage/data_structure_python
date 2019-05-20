def heap_sort(seq): # 实现由小到大排序，以>=为优先度高
    n = len(seq)
    def shiftdown(e, start, end):
        i ,j = start, 2*start + 1
        while j < end:
            if j + 1 < end and seq[j+1] > seq[j]:
                j += 1
            if e >= seq[j]:
                break
            seq[i] = seq[j]
            i, j = j, 2*j + 1
        seq[i] = e
    for i in range(n//2-1, -1, -1):
        shiftdown(seq[i], i, n)
    for i in range(n-1, 0, -1):
        e = seq[i]
        seq[i] = seq[0]
        shiftdown(e, 0, i)
    return seq
    
if __name__ == '__main__':
    from random import randint
    seq = [randint(0,100) for _ in range(10)]
    print(seq)
    print(heap_sort(seq[:]))