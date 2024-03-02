def recursive_addition(num):
    # base case
    if num == 0:
        return 0
    # recursive case
    else:
        return num + recursive_addition(num-1)

result = recursive_addition(10)
print(result)