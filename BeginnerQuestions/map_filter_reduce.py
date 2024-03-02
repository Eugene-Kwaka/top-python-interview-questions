# # map(function, iterable)
# def square_num(num):
#     return num**2

# numbers = [1,2,3,4,5]
# squared_nums = map(square_num, numbers)
# print(tuple(squared_nums))

#FILTER FUNCTION
# def is_even(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))
# With a lambda function
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_numbers = filter(lambda x: x % 2 == 1, numbers)
# print(set(odd_numbers))

#REDUCE
# python code to demonstrate working of reduce()
# importing functools for reduce()
import functools
numbers = [1, 2, 3, 4, 5, 6,]
max_num = functools.reduce(lambda a, b: a if a > b else b, numbers)
# using reduce() to compute maximum element from numbers
print(f"The maximum element of the list is {max_num}")
# using reduce() to compute sum of numbers
sum = functools.reduce(lambda a, b: a+b, numbers)
print(f"The sum of the list elements is {sum}")
 
