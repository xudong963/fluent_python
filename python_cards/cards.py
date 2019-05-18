# Container Datatypes
# This module implements specialized container datatypes providing alternatives to
# Python’s general purpose built-in containers,dict, list, set, and tuple.
import collections

# 随机抽取
from random import choice

# Returns a new tuple subclass named typename.
# The new subclass is used to create tuple-like objects that have fields accessible by attribute
# lookup as well as being indexable and iterable.
Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(deck.ranks)
print(deck.suits)
print(deck._cards)
print(len(deck), deck.__len__())     # 没有my_object.__len__的写法,在执行len(my_object)的时候，python会自己去调用__len__方法

# 如果没有了特殊方法__getitem__,deck[]不能使用
print(deck[0], deck.__getitem__(0))
print(choice(deck))

# 切片操作
print(deck[:3])

# 先取出位置在12的那张牌,然后每隔13取一次
print(deck[12::13])

# 由于__getitem__方法的实现,可迭代了
for card in deck:
    print(card)

# 反向迭代
for card in reversed(deck):
    print(card)

print('---------------------------------------------------------------------------')

# 进行排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    # list的index方法，用于找到某个值第一个匹配项的索引位置
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)













