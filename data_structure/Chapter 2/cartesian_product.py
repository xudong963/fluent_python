# 用listcomps生成两个或两个以上的可迭代类型的笛卡儿积

colors = ['black', 'white']
sizes = ['s', 'm', 'l']

# 先以颜色排列，在以尺码排列
tshirts = [(color, size) for color in colors for size in sizes]   
print(tshirts)

# 传统的for实现
for color in colors:
    for size in sizes:
        print((color, size))


# 先以尺码排列，在以颜色排列
tshirtss = [(color, size) for size in sizes for color in colors]
print(tshirtss)

