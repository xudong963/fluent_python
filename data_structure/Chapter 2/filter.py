# the filter() method filters the given iterable with the help of 
# a function that tests each element in the iterable to be true or not.
# syntax : filter(function, iterable)

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print(type(filteredVowels))
print(list(filteredVowels))
print(set(filteredVowels))

print('The filtered vowels are:')
for vowel in filter(filterVowels, alphabets):
    print(vowel)