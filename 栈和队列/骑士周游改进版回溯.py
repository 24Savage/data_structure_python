import turtle

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
    turtle.setworldcoordinates(-0.5,-0.5,n,n)
    draw_board(n)
    turtle.tracer(1)
    turtle.goto(path[0][0],path[0][1])  # 移动到起点
    turtle.pendown()
    for pos in path:
        turtle.goto(pos[0],pos[1])
    turtle.Screen().exitonclick()
    
def knight(x,y,n):  #(x,y)出发坐标, n*n的棋盘
    dx=(1,2,2,1,-1,-2,-2,-1)
    dy=(2,1,-1,-2,-2,-1,1,2)    #不同方位的坐标变换
    board=[1]*(n**2) # 模拟棋盘，用1表示位置空闲
    board[x*n+y]=0
    st=list()
    st.append((x,y))
        
    def list_of_next(pos):  # 返回pos坐标的可行目标点列表
        arr=[]
        x,y=pos[0],pos[1]
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx*n+ny]==1:
                arr.append((nx,ny))
        return arr
        
    def get_best_next(pos): # 返回分支最少的下一个点
        temp = 9
        best = None
        arr = list_of_next(pos)
        for i in arr:
            num = len(list_of_next(i))
            if num < temp:
                temp = num
                best = i
        return best
    
    while st:
        if len(st)==n**2:
            draw(st)
            break
        pos=st[-1]
        x,y=pos[0],pos[1]
        best=get_best_next(pos)
        if best:
            nx,ny=best[0],best[1]
            board[nx*n+ny] = 0
            st.append(best)

knight(3,3,7)