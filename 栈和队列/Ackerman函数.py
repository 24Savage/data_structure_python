def Ack(m,n):
    # val[i] = ack(i,ind[i])
    ind=[-1]*(m+1)
    val=[-1]*(m+1)
    ind[0]=0
    val[0]=1
    while ind[m]<n:
        ind[0]+=1
        val[0]+=1
        for j in range(m):
            if ind[j]==1:
                val[j+1]=val[j]
                ind[j+1]=0
            elif val[j+1]==ind[j]:
                ind[j+1]+=1
                val[j+1]=val[j]
            else:
                break
    return val[m]

def ack(m,n):
    st=list()
    st.append(m)
    while st:
        m=st.pop()
        if not m:
            n+=1
        elif n:
            n-=1
            st.append(m-1)
            st.append(m)
        else:
            st.append(m-1)
            n=1
    return n


print(Ack(4,3))