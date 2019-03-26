#list
def list_demo():
    alist1 = [1,2,3,4,'一','abc']
    print(alist1)
    return alist1

def list_demo2():
    alist1 = list_demo()
    print(alist1)
    alist1[0]=7
    print(alist1.pop())
    print(alist1)
    alist1.pop(4)
    print(alist1)

#循环
def for_demo():
    for i in range(5):    #从0数到4
        print('hello world')

    for i in range(3,7):    #从3数到6
        print(i)

    for i in range(3,10,2):    #从3数到9,步长2
        print(i)

    for i in range(10,3,-1):    #从10数到4,倒着数
        print(i)

#用range和list控制函数循环

def for_list():
    alist = ['我','你','他','老王','老闫']
    for i in range(5):
        print(i)
        print(alist[i])     #取下标
    print('=======================')
    for i in alist:   #非常简单的写法,效果一模一样,固定语法,没有为什么
        print(i)

if __name__ == '__main__':
    for_list()