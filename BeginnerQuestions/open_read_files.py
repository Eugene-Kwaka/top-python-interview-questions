# Open the file in read mode
file = open("file.txt", "r")

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Print the contents of the file
print(contents)

# # File is in a different Path
# f = open(r"C:\\myfiles\file.txt", "r")

file = open("file.txt", "r")

for line in file:
    print(line)

file.close()