def count_vowels(string):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    # Initialize a counter for vowels
    vowel_count = 0
    # Iterate over each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            # If char is a vowel, increment the vowel count
            vowel_count += 1
    # Return the total number of vowels
    return vowel_count

# Test the function
string = input("Enter a string: ")
print("The number of vowels is:", count_vowels(string))