# generator expression

alphabets = "ABCDEF"

# 生成器表达式是函数调用的唯一参数，不需要用额外的括号将它括起来
tup = tuple(ord(alphabet) for alphabet in alphabets)
print(tup)


import array
# 两个参数，将生成器表达式括起来
arr = array.array('I', (ord(alphabet) for alphabet in alphabets))
print(arr)


generator_expression = (ord(alphabet) for alphabet in alphabets)
print(type(generator_expression))
# output: <class 'generator'>   generator is a iterable
# 所以生成器表达式更节省内存




# 笛卡儿积
colors = ['black', 'white']
sizes = ['s', 'm', 'l']

# 生成器表达式可以省去for循环的开销，即列表
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
