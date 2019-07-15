# 字典在python中十分重要,是python的基石,python对它的实现做了高度优化
# 散列表是让字典类型性能出众的根本原因
# 用isinstance 来检查某个类型是不是dict类型

my_dict = {}
print(isinstance(my_dict, dict))

# 标准库里所有的映射类型都是用dict实现的
# 它们有个共同的要求：只有可散列的数据类型才能用作这些映射里的键

# 可散列数据类型：如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，
# 而且这个对象需要实现 __hash__() 方 法。另外可散列对象还要有 __qe__() 方法，这样才能跟其他键做比较。
# 如果两个可散列对象是相等的，那么它们的散列值 一定是一样的

# 原子不可变数据类型(str,bytes,数组类型)都是可散列的,frozenset也是可散列的
# frozenset : return
# 对于元组，只有当一个元组包含的所有元素都是可散列类型的情况下，它才是可散列的


tt = (1, 2, (30, 40))
print(hash(tt))

tl = (1, 2, [30, 40])
# print(hash(tl))  error: list is unhashable type

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))


# dict的构造方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict({'three': 3, 'two': 2, 'one': 1})
e = dict((('one', 1), ('two', 2), ('three', 3)))
print(a==b==c==d==e)
print(a)
print(b)
print(c)
print(d)
print(e)




l = zip(['one', 'two', 'three'], [1, 2, 3])
print(list(l))

t = zip(['one', 'two', 'three'], [1, 2, 3])
print(tuple(t))

d = zip(['one', 'two', 'three'], [1, 2, 3])
print(dict(d))

s = zip(['one', 'two', 'three'], [1, 2, 3])
print(set(s))






