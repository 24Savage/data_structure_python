import turtle
turtle.setworldcoordinates(-0.5,-0.5,8,8)

def draw_block(x,y):    # 绘制棋盘格的方块
    turtle.goto(x+0.5,y-0.5)
    turtle.pendown()
    turtle.setheading(90)
    for i in range(4):
        turtle.forward(1)
        turtle.left(90)
    turtle.penup()

def draw_board(n):   # 绘制n*n棋盘格
    turtle.tracer(0)
    turtle.penup()
    for y in range(n):
        for x in range(n):
            turtle.goto(x,y)
            draw_block(x,y)
            
def draw(path):
    n=int(len(path)**0.5)
    draw_board(n)
    turtle.tracer(1)
    turtle.goto(path[0][0],path[0][1])  # 移动到起点
    turtle.pendown()
    for pos in path:
        turtle.goto(pos[0],pos[1])
    turtle.Screen().exitonclick()
    
def knight(x,y,n):  #(x,y)出发坐标, n*n的棋盘
    '''
    回溯法求解出骑士周游的解'''
    dx=(1,2,2,1,-1,-2,-2,-1)
    dy=(2,1,-1,-2,-2,-1,1,2)    #不同方位的坐标变换
    board=[0]*(n**2) # 模拟棋盘，用0表示位置空闲
    board[x*n+y]=1
    st=list()
    st.append((x,y,0))
    recur_step=0
    while st:
        x,y,nxt=st.pop()
        while nxt<8:
            nx=x+dx[nxt]
            ny=y+dy[nxt]
            if 0<=nx<n and 0<=ny<n and not board[nx*n+ny]:   # 新位置存在且没有走过
                #if recur_step !=0:
                    #print('回溯过%s步,回溯前的路径长度%s'%(recur_step,len(st)+recur_step))
                    #recur_step=0
                board[nx*n+ny]=1
                st.append((x,y,nxt+1))
                st.append((nx,ny,0))
                break
            nxt+=1
        if nxt==8:
            #recur_step+=1
            board[x*n+y]=0
            continue
        if len(st)==n*n:
            draw(st)
            break # 得到了一个解

knight(3,3,7)
turtle.Screen().exitonclick()