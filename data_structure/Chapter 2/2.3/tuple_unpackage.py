# 平行赋值

lax_coordinates = (33.924, -118.10)
latitude, longitude = lax_coordinates
print(latitude, longitude)


# 交换两个变量的值
a = 5
b = 6
b, a = a, b
print(a, b)

# 用*运算符把一个可迭代的对象拆开作为函数的参数

t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

# 让一个函数可以用元组的形式返回多个值
# 对于不感兴趣的部分，占位符_很好用
import os
_, filename = os.path.split('/home/code/python/1.py')
print(filename)


# 用*运算符来处理剩下的元素
a, b, *rest = range(5)
print(a, b , rest)

a, *body, c, d = range(5)
print(a, body, c, d)




