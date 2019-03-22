# 步长
# for语句

def list_bianli():
    for i in range(10):
        a=0
        a+=1
        print(i)
        print(a)

def list_bianli1():
    alist=['啊','第三方','尔尔','玩儿']
    for i in alist:
        print("--遍历")
        print(i)
        print(i+'__hello')

def nei_xunhuan():
    for i in range(5):
        print('hello world')
        for j in range(2):
            print('内循环')

def chengfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s X %s = %s' %(i,j,i*j),end='   ')
        print(' ')

# 基本 if else 语法演示
def if_demo():
    a = False
    if a :
        print('a是对的')
    else:
        print('a是错的')

# if else语法原理
def if_demo0():
    if False :
        print('正确')
    else:
        print('错误')

# 判断 a 和 b的大小
def if_demo1():
    a=10
    b=20
    if a>b:
        print('a大于b')
    else:
        print('a小于b')

# 输出 比较大的值
def if_demo2():
    a=10
    b=20
    if a>b:
        print(a)
    else:
        print(b)

# 三个条件判断,不符合走else分支
def elif_demo():
    a=4
    if a==2:
        print('第1个if')
    elif a==3:
        print('第2个if')
    elif a==1:
        print('第3个if')
    else:
        print('else分支')

# 将1到50的奇数加起来
def jishu():
    num=0
    for i in range(1,51):
        if i%2 != 0:
            num=num+i
    print(num)

# 周末作业:2个int参数之间的偶数加起来
def zhoumozuoye():
    a=4
    b=10
    num=0
    for i in range(a+1,b):
        if i%2 ==0:
            num=num+i
    print(num)

if __name__ == '__main__':
    zhoumozuoye()
