def is_palindrome(string):
    # Returns True if the given string is a palindrome, False otherwise.
    reverse_string = string[::-1]
    return string == reverse_string

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"The string {input_string} is a palindrome")
else:
    print(f"The string {input_string} is not a palindrome")