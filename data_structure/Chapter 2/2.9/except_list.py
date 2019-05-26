# 数组
# 如果我们需要一个只包含数字的列表,array.array比 list高效
# 支持.pop、.insert等
# 数组还提供了从文件读取和存入文件的更快的方法,.frombytes和.tofile


from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
# 'd'是 type code
print(floats[-1])
print(type(floats[-1]))

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print (floats==floats2)


# array不再支持就地排序
# 需要这样做
a = array('i', (5, 6, 4, 1))
a = array(a.typecode, sorted(a))
print(a)
