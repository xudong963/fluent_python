# memoryview是一个内置类，它可以让用户不复制内容的情况下操作同一个数组的不同切片
# 内存视图其实是泛化和去数学化的Numpy数组
# memory.cast的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意移动


# 利用memory.cast精准地修改了一个数组中的某个字节。

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)
print(memv)  # output: <memory at 0x0000026CA6949408>
