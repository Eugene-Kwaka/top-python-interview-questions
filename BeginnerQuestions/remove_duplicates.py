def remove_duplicates(lst):
    # create an empty set to store unique elements
    new_set = set()

    # loop through the list, adding each element to the set
    # sets only store unique elements, so duplicates will be automatically removed
    for item in lst:
        new_set.add(item)

    # convert the set back to a list
    return list(new_set)

# For example
lst = [1, 2, 3, 2, 1, 4, 5, 3, 6]
new_lst = remove_duplicates(lst)
print("Original list:", lst)
print("List with duplicates removed:", new_lst) 