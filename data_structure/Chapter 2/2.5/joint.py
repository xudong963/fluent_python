weird_board = [ ['_']*3 ] * 3
print(weird_board)
# output : [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# 外面的列表实际上包含3个指向同一列表的引用


weird_board[1][2] = 0
print(weird_board)
# output : [['_', '_', 0], ['_', '_', 0], ['_', '_', 0]]


board = [ ['_']*3 for i in range(3) ]
print(board)
# output : [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


board[1][2] = 0
print(board)

# output: [['_', '_', '_'], ['_', '_', 0], ['_', '_', '_']]




# 还有一个例子
origin = ['_'] * 3
new = []
for i in range(3):
    new.append(origin)
new[2][0] = 0
print(new)


New = []
for i in range(3):
    Origin = ['_'] * 3
    New.append(Origin)
New[2][0] = 0
print(New)
