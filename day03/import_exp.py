import os

def os_demo():
    getcwd = os.getcwd()    #获取当前路径
    print(getcwd)
    abspath = os.path.abspath('..')     #..代表返回上级目录
    print(abspath)
    abspath1 = os.path.abspath('../..')     #../..返回上级的上级目录
    print(abspath1)

def open_demo():
    # 相对路径  ../test.text
    # 绝对路径  C:\Users\Administrator\PycharmProjects\myedu\day03\test.text
    # open('test.text','w+')
    # text_io = open('../test.text','w+')
    text_io = open('../test.text','a+')
    text_io.write("XXXXX")

def openr_demo():
    text_io = open('../test.text','r')
    readline = text_io.readline(4)
    print(readline)
    readlines = text_io.readlines()
    print(readlines)

if __name__ == '__main__':
    open_demo()
