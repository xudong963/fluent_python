# 映射类型：dict, collections.defaultdict, collections.OrderedDict, collection.ChainMap
# defaultdict 是内置dict的子类。它重载了一个方法，并添加了一个可写的实例变量
from collections import defaultdict, OrderedDict
s = (('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1))
d = defaultdict(list)  
for k, v in s:
    d[k].append(v)    # 通过default_factory方法，返回一个[],然后list.append()添加一个值到列表中
print(d)

# 与上面等效的操作
dd = {}
for k, v in s:
    dd.setdefault(k, []).append(v)
print(dd)
print(dd)

str = 'mississippi'
dStr = defaultdict(int)
for c in str:
    dStr[c]+=1
print(dStr)




od = OrderedDict([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])
print(od)
print(len(od))
print(od['yellow'])
print('yellow' in od)
# popitem(last=True) 函数
# 如果last为真，则后进先出，类似于栈
# 否则，先进先出
od.popitem()  
print(od)
od.popitem(False)
print(od)



# 一个chainMap,将多个字典或者映射组合在一切,创建一个单独的可更新的视图
# 这个类可以用于模拟嵌套作用域，并且在模板化的时候比较有用。
# 待续.....