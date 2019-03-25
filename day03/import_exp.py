import os

def os_demo():
    getcwd = os.getcwd()    #获取当前路径
    print(getcwd)
    abspath = os.path.abspath('..')     #..代表返回上级目录
    print(abspath)
    abspath1 = os.path.abspath('../..')     #../..返回上级的上级目录
    print(abspath1)

if __name__ == '__main__':
    # 相对路径  ../test.text
    # 绝对路径  C:\Users\Administrator\PycharmProjects\myedu\day03\test.text
    # open('test.text','w+')
    text_io = open('../test.text','w+')
    text_io.write("XXXXX")
    pass



