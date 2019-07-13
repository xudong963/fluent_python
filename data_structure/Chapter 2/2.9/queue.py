# collections.deque类(双向队列)是一个线程安全，可以快速从两端添加或者删除元素的数据类型。

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

# 当n>0时，将队列右边的n的元素移动到左边
dq.rotate(3)    # 返回None, 就地变动
print(dq)

# 当n<0时，将队列左边的-n个元素移动到右边
dq.rotate(-3)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extendleft([-2, -3, -4])
print(dq)

print(dq.popleft())
print(dq)

print(dq.pop())
print(dq)
 
dq.remove(0)      # remove(e) 移除第一次出现的e元素
print(dq)
