
import json
# 声明一个全量 dict 变量 （字典）

adict = {"name":"ysl","pwd":"123456",1:"数字1"}

# 这是一个字符串 不过他是json格式，也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456","1":"数字1"}'

def zhuanhuanleixin():
    # 打印adictStr变量的类型
    print(type(adictStr))
    # 将adictStr转换为dict格式 并赋值给dict_str
    dict_str = json.loads(adictStr)
    # 打印dict_str 变量的类型
    print(type(dict_str))
    # 打印 dict_str 字典中 key 为 name 的值
    print(dict_str['name'])

if __name__ == '__main__':
    # print(adict)
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)

    # 字符串转dict
    loads = json.loads(adictStr)
    print(type(loads))

    # 字典转字符串 不处理编码格式
    json_dumps = json.dumps(loads)
    print(json_dumps)

    # 字典转字符串，ensure_ascii=False 指定编码格式 不为ASCII码
    dumps = json.dumps(loads,ensure_ascii=False)
    print(dumps)

    # str类型和dict类型之间的转换
    #print(type(adictStr))
    #print(type(adict))

    # str --> dict（使用json,loads）
    #loads = json.loads(adictStr)  # 这一步将adictStr（str格式）转换为dict格式，并赋值给了loads这个变量，原本adictStr依旧是string格式
    #print(type(loads))        # 试一下loads的格式，如果是dict格式那就对了
    #print(loads['name'])     # 对于dict格式，打印name['key']结果就是value，就和json格式一样，键值对key=value
    #print(loads['pwd'])      # 和上一条同理

    # dict --> str（使用json.dumps）
    #dumps = json.dumps(adict)
    #print(type(dumps))

