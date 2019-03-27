# 声明类 class 声明方法 def
# class 类
# object 对象 / 或者所有父类

# 声明类的语法：class：就是声明一个类；Human：类的名字（）：括号里面填 这个类的父类
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


if __name__ == '__main__':
    human = Human('ysl',25,'男')
    human.myInfo()

