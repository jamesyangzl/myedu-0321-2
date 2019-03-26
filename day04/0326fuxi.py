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

#assert
def assert_demo():
    assert 4>2
    #assert 1>2
    astr='你好世界'
    assert '你'in astr
    #assert '我'in astr
    assert '你'not in astr

#if,else,elif
def if_demo():
    a = 12
    b = 12
    if a>b:
        print('a大于b')
    elif a<b:
        print('a小于b')
    else:
        print('a等于b')

#while
def while_demo():
    a=0
    while a<5:
        print(a)
        # a+=1
        a+=2
#while 不如for循环,一般就不用了


def try_demo():
    astr = 'gsdfhser'
    try:
        assert '你' in astr
    except:
        print('报错啦,断言没通过')
    print('-------')
#try用来处理异常,不会一出现异常就停止

if __name__ == '__main__':
    try_demo()





