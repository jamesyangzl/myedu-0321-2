# 步长

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

if __name__ == '__main__':
    chengfabiao()

