# # CONTINUE
# # loop from 1 to 5
# for i in range(1, 6):
   
#     # If i is equals to 3, continue to next iteration without printing 
#     if i == 3:
#         continue
#     else:
#         # print value of i
#         print(i)
        
# # BREAK STATEMENT
# s = 'LambdaTest'
# # Using for loop
# for letter in s:
#     print(letter)
#     # break the loop as soon it sees 'b'
#     if letter == 'b':
#         break
   
# print("Exits the for loop")
   
# i = 0
# # Using while loop
# while True:
#     print(s[i])
#     # break the loop as soon it sees 'b'
#     if s[i] == 'b':
#         break
#     i += 1
   
# print("Exits of while loop")

# PASS STATEMENT
s = "LambdaTest"

# Empty loop
for i in s:
    pass
 
# Empty function
def function():
    pass
 
# No error will be raised
function()
 
# Pass statement
for i in s:
    if i == 'b':
        pass
        print('Nothing happens. Pass executed')