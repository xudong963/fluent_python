# map function return a list of the results after applying the given function
# to each item of a given iterable(lis,tuple etc)
# The returned value from map() (map object) then 
# can be passed to functions like list() (to create a list), set() (to create a set) and so on.
# map(func, iter)

numbers = (1,2,3,4)

result = map(lambda x : x+x, numbers)
print(type(result))
print(set(result))
print(list(result))

for i in map(lambda x : x+x, numbers):
    print(i)
