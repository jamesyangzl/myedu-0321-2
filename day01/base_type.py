# 这是一个注释
# model 模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# 代码的层级关闭关系 通过 缩进来表示
# class 类，类型
# str string 字符
# 合法标识符（变量名方法名）：必须字母或_开头，剩下的可以是字母数字，下划线，大小写敏感，不可用关键字（python自带单词，比如def，if，pass）做标识符
# ctrl+alt+l 格式化代码

# 声明一个int_demo方法 没有参数
def int_demo():
    # 声明aint变量，并赋值1，打印aint的值和aint的类型
    aint = 1
    print(aint)
    print(type(aint))

# 声明一个str_demo方法
def str_demo():
    # 声明aint变量，并赋值'1'（由于是字符串要加''），打印astr的值和类型
    astr = '1'
    print(astr)
    print(type(astr))

def str_demo1():
    a= 'hello'
    b= 'world'
    return a+b

def str_demo2():
    a= 'hello'
    b= 250
    s = str(b)
    print(s)
    print(type(s))
    print(a+s)

# 声明一个float_demo方法 没有参数
def float_demo():
    # 声明afloat变量，并赋值1.90，打印afloat的值和类型
    afloat = 1.91
    print(afloat)
    print(type(afloat))

# 声明一个add（加法）方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数和bint参数并返回aint加bint的结果
    print(aint)
    print(bint)
    return aint + bint

# 声明一个sub（减法）方法 参数有两个 aint,bint
def sub(aint, bint):
    # 打印aint参数和bint参数并返回aint减bint的结果
    print(aint)
    print(bint)
    return aint - bint

if __name__ == '__main__':
    print(str_demo2())
    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量 ctrl+alt+v
    # 调用add方法 传入1,2，得到返回值，赋值“=”给result变量
    # result = sub(3, 4)
    # print(result)
    pass
