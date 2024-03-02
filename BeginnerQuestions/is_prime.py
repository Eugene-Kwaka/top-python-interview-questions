def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is prime
    if num == 2:
        return True

    # check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False
        # if num is not divisible by any number from 2 to num-1, then it is prime
        else:
            return True

print(is_prime(8))
print(is_prime(131))