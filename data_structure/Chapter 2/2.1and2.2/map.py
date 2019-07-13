# map function return a iterable after applying the given function
# to each item of a given iterable(lis,tuple etc)
# map(function, iterable)

numbers = (1,2,3,4)
print(set(numbers))
result = map(lambda x : x+x, numbers)

print(type(result))
print(set(result))
print(list(result))

for i in map(lambda x : x+x, numbers):
    print(i)

# 下面是很重要的

# 关于运行结果的解释：
# <class 'map'>   :map()返回的是一个iterable,不是list等，而map object就是 iterable 所以<class 'map'>
# {8, 2, 4, 6}    :set()的参数是iterable,所以可以把result传进去,然后迭代产生{8, 2, 4, 6},此时result已经到了末尾,类似于c++的end()
# []: 由于result已经到了末尾，所以自然产生[]