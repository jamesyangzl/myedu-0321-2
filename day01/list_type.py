def list_demo():
    alist = [4, 'ysl', '8', 7]
    print(alist)
    # 通过索引访问 元素
    print(alist[0])
    print(alist[1])
    # 倒序访问
    print(alist[-1])
    print(alist[-2])

# 更新列表中的元素
def list_update(alist):
    alist[0] = 1
    print(alist[0])
    print(alist)

# 切片操作
def list_update1(alist):
    # 从索引2 的位置 取 到索引5
    print(alist[2:6])
    # 从索引0 的位置 取 到索引5
    print(alist[:6])
    # 从索引3 的位置 取 到索引末尾
    print(alist[3:])

blist = [8,7,6,5,4]

# 删除方法 list.pop()
def pop_demo(alist):
    # pop()方法两个作用 第一个取出最后一位的值，第二个从列表中删除取出的值
    print(alist.pop())
    print(alist)
    # pop()带参数，参数被用作 下标值/索引，两个作用 第一个取出下标值代表的元素，第二个从列表中删除取出的元素
    alist.pop(4)
    print(alist)

# 将列表排序的方法
def orderBy_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()

# 正序方法
def sort_demo():
    # 将blist 正序排
    blist.sort()
    print(blist)

# 倒序方法
def reverse_demo():
    # 将blist 倒序排
    blist.reverse()
    print(blist)

# 列表/集合
if __name__ == '__main__':
    alist = [4, 'ysl', '8', 7,6,2,5]
    # note='全局'
    # refer = str(blist[0])
    # print(note+refer)
    # print(note)
    # print(blist)
    # print(blist[0:2])
    # list_update(alist)
    # print(len(alist))
    # print(len(blist))
    # pop_demo(alist)



