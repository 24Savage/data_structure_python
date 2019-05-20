class Stack:
    '''
    虽然列表可以达到同样的效果，但是同时提供了栈所不支持的其他操作，影响安全性'''
    def __init__(self):
        self.__stack=list()
    @property
    def top(self):
        return self.__stack[-1]
    def pop(self):
        return self.__stack.pop()
    def push(self,val):
        self.__stack.append(val)
    @property
    def depth(self):
        return self.__stack.__len__()

def cal(n1,n2,op):
        n1,n2=float(n1),float(n2)
        if op=='+':
            return str(n1+n2)
        if op=='-':
            return str(n2-n1)
        if op=='*':
            return str(n1*n2)
        if op=='/':
            return str(n2/n1)
        
def calculate_suffix(exp):
    '''
    计算后缀表达式'''
    operands=Stack()
    operators='+-*/'
    for x in token(exp):
        if x not in operators:
            operands.push(x)
        else:
            if operands.depth<2:
                raise SyntaxError('expression SyntaxError')
            n1,n2=operands.pop(),operands.pop()
            operands.push(cal(n1,n2,x))
    if operands.depth==1:
        return operands.pop()
    raise SyntaxError
    
def calculate_infix(exp):
    '''
    计算中缀表达式
    目前不能处理负数'''
    operands,st=Stack(),Stack()
    priority={'(':0,'+':1,'-':1,'*':2,'/':2}
    operators='+-*/()'
    for x in token(exp):
        if x not in operators:
            operands.push(x)
        elif x=='(' or not st.depth:
            st.push(x)
        elif x==')':
            while st.depth and st.top!='(':
                op=st.pop()
                if operands.depth<2:
                    raise SyntaxError('expression SyntaxError')
                n1,n2=operands.pop(),operands.pop()
                operands.push(cal(n1,n2,op))
            if not st.depth:
                raise SyntaxError('missing (')
            st.pop()
        else:
            while st.depth and priority[st.top]>=priority[x]:
                op=st.pop()
                if operands.depth<2:
                    raise SyntaxError('expression SyntaxError')
                n1,n2=operands.pop(),operands.pop()
                operands.push(cal(n1,n2,op))
            st.push(x)
    while st.depth:
        if st.top=='(':
            raise SyntaxError('missing )')
        op=st.pop()
        if operands.depth<2:
            raise SyntaxError('expression SyntaxError')
        n1,n2=operands.pop(),operands.pop()
        operands.push(cal(n1,n2,op))
    return operands.pop()

def token(exp):
    '''
    生成器函数
    此函数的作用是逐个输出表达式中的各项
    规定表达式的各项以空格分隔，或各项紧贴'''
    i,leng=0,len(exp)
    operators='+-*/()'
    pn='+-'
    while i<leng:
        while i<leng and exp[i].isspace():
            i+=1
        if i==leng:
            break
        if exp[i] in operators:
            '''检测是否存在正负,存在正负号的情况如下,
            【1】运算符(+-*/后跟正负号
            【2】开头存在正负号
             只在中缀转后缀、前缀中有用，因为无法区分后缀中2 -6中的-6'''
            if exp[i] in pn:
                t=i-1
                while t>=0 and exp[t].isspace():    # +-左边第一个字符是否为运算符
                    t-=1
                if t==-1 or exp[t] in '(+-*/':
                    s=i
                    while i<leng-1 and exp[i+1] not in operators and not exp[i+1].isspace():  # 与+-紧邻的是否为运算对象
                        i+=1
                    yield exp[s:i+1]
                    i+=1
                    continue
                else:
                    yield exp[i]
                    i+=1
                    continue
            yield exp[i]
            i+=1
            continue
        start=i
        i+=1
        while i<leng and exp[i] not in operators and not exp[i].isspace():
            if exp[i] in 'Ee' and i+1<leng and exp[i+1]=='-':
                i+=1
            i+=1
        yield exp[start:i]

def in_to_suf(infix):
    '''
    此函数的作用是将中缀表达式转换成后缀表达式'''
    priority={'(':0,'+':1,'-':1,'*':2,'/':2}
    operators='+-*/()'
    suf=list()
    st=Stack()
    for i in token(infix):
        if i not in operators:
            suf.append(i)
        elif i=='(' or (st.depth==0 and i!=')'): # i!=')'是为了避免在首字符为)时异常提示不正确
            st.push(i)
        elif i==')':
            while st.depth and st.top!='(':
                suf.append(st.pop())
            if not st.depth:
                raise SyntaxError('syntaxerror: missing ( !')
            st.pop()
        else:
            while st.depth and priority[i]<=priority[st.top]:
                suf.append(st.pop())
            st.push(i)
    while st.depth:
        if st.top=='(':
            raise SyntaxError('syntaxError: missing )')
        suf.append(st.pop())
    return ' '.join(suf)

def in_to_pre(infix):
    '''
    将中缀表达式转换成前缀表达式'''
    pre,st=list(),Stack()
    operators='+-*/()'
    priority={')':0,'+':1,'-':1,'*':2,'/':2}
    for x in list(token(exp))[::-1]:
        if x not in operators:
            pre.append(x)
        elif x==')' or (st.depth==0 and x!=')'):
            st.push(x)
        elif x=='(':
            while st.depth and st.top!=')':
                pre.append(st.pop())
            if st.depth==0:
                raise SyntaxError('missing )')
            st.pop()
        else:
            while st.depth and priority[x]<=priority[st.top]:
                pre.append(st.pop())
            st.push(x)
    while st.depth:
        if st.top==')':
            raise SyntaxError('missing (')
        pre.append(st.pop())
    return ' '.join(pre[::-1])
    
exp='(7+4)*(2-6/-3)+4'
pre=in_to_pre(exp)
suf=in_to_suf(exp)
print(pre,'\n',suf)