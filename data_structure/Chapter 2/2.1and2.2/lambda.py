# also called anonymous function
# syntax: lambda arguments: expression
# The expression is evaluated and returned.
# Lambda functions are used along with built-in functions like filter(), map() etc.


double = lambda x : x+x
print(double(5))
# Output: 10

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)