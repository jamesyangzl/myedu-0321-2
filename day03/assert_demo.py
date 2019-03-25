
def assert_true():      #true不会报错
    assert True

def assert_false():     #false会响应直接报错
    assert False

def assert_demo():      #a里面没有7所以报错
    a="123456"
    assert '7' in a
    print('----')

def assert_demo2():     #a里面有6所以不报错
    a="123456"
    assert '6' in a
    print('----')

def assert_demo3():     #报错
    a="123456"
    b=None
    print(a+b)

def assert_demo4():     #用try语句即使报错但依旧输出结果
    a="123456"
    try:
        assert '7' in a
    except:
        print('a里面没有7')
    print('-------')

def assert_demo5():     #try之内的正确就不会输出except内的内容
    a="123456"
    try:
        assert '6' in a
    except:
        print('a里面没有7')
    print('-------')

def assert_demo6():     #不管是否出错,都会执行finally
    a="123456"
    try:
        assert '6' not in a
    # except:
    #     print('a里面没有7')
    finally:
        print('最后----')

if __name__ == '__main__':
    assert_demo6()








