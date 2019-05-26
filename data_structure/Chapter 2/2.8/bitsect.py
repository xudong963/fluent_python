# 使用bitsect管理已经排序的序列

# bisect模块有两个主要函数, bisect 和 insort
# 两个函数均利用二分查找算法在有序序列里查找和插入元素

from bisect import bisect
from bisect import insort  
# 不可以单纯的import bisect
# 如果单纯导入的话,需要这样写: bisect.bisect()

# bisect(haystack, needle) 在 haystack 中搜索needle的位置
# 该位置满足的条件是,把needle插入这个位置后，haystack还能保持升序

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30] 
needles= [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
position = []

for needle in reversed(needles):
    position.append(bisect(haystack, needle))

print(position)


# 用bisect.insort插入新元素

insort(haystack, 13)
print(haystack)