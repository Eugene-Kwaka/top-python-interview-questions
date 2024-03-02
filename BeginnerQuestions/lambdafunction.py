# lambda arguments: expression

# Using a lambda function to double a number
lambda_double = lambda x: x*2
print(lambda_double(5)) # output is 10

numbers = [1, 2, 3, 4, 5]
double_numbers = map(lambda_double, numbers)
print(list(double_numbers))