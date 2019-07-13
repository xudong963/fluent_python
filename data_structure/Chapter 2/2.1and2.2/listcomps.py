# show advantage of listcomps

alphabets = 'ABCDEFG'

# listcomps
beyond_ascii1 = [ord(alphabet) for alphabet in alphabets if ord(alphabet) > 68]

# map, filter, lambda
beyond_ascii2 = list(filter(lambda x: x > 68, map(ord, alphabets)))

print(beyond_ascii1)
print(beyond_ascii2)