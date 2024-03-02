# # Syntax for Shallow Copy
# original_list = [[1, 2, 3], 4, 5, 6, 7, 8, 9]
# shallow_copy = original_list.copy()

# # changing an element in the copied object
# shallow_copy[0][1] = "changed"
# print("The original list:", original_list)
# print("The copied list: ", shallow_copy)

# DEEP COPY
import copy

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_copy = copy.deepcopy(original_list)
# changing an element in the copied object
deep_copy[0][1] = "altered"
print(original_list) 
print(deep_copy)