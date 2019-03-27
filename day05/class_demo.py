# 声明类 class 声明方法 def
# class 类
# object 对象 / 或者所有父类
# 面向对象编程

# 声明类的语法：class：就是声明一个类；Human：类的名字（）：括号里面填 这个类的父类
# class Human: （不写的话就自动继承object类）
class Human(object):

    # 类的初始化方法 self：就代表类 本身
    def __init__(self,name,age,sex):
        # 将入参的name 赋值类 类本身的name
        self.name = name
        self.age = age
        self.sex = sex

    # 类里面的方法 必传self（类本身）
    def myInfo(self):
        print('我叫%s，我今年%s岁，%s'%(self.name, self.age, self.sex))

    def myInfoStr(self):
        return '我叫%s，我今年%s岁，%s'%(self.name, self.age, self.sex)

# 声明一个测试者 类，继承 Human类
class Tester(Human):
    # 声明了一个方法
    def zhiXingCeShi(self):
        # 调用了父亲的属性
        print(self.name)
        print('我在执行测试，别打扰我')

if __name__ == '__main__':
    # = 后面 调用这个类 传入了 初始化的参数，参数必须传，而且传完整
    # = 前面 是 对象名
    # 对象 是 类的 实例化， 对象是变量的一种（类到对象，就是实例化的过程）
    # human = Human('ysl',25,'男')
    # print(type(human))
    # # 对象可使用 类中的方法
    # human.myInfo()
    # info_str = human.myInfoStr()
    # print(human.myInfoStr())
    # print(info_str)


    # 继承就是多态的一种表现方式，新建对象
    tester = Tester('ysl',25,'男')
    # 对象可使用 类中的方法
    tester.zhiXingCeShi()

