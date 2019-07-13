# list.sort方法会就地排序列表，也就是说不会把原列表进行复制
# 通:如果一个的函数或者方法对对象进行就地改动,那么将会返回None，说明没有产生新对象

# 返回none有一个缺点,就是无法将其串联起来使用,而返回一个新对象的方法
# 则正好相反(比如str中的所有方法)

# 内置函数sorted则正好相反,它会返回一个列表。

# 两个函数均有的关键字

# reverse 默认False
# key 一个只要一个参数的函数,这个函数会应用于序列中的每一个元素

# example
fruits = [ 'grape', 'rasberry', 'apple', 'banana' ]
print(sorted(fruits))
print(fruits)

print(sorted(fruits, reverse = True))
print(sorted(fruits, key = len))

fruits.sort()
print(fruits)