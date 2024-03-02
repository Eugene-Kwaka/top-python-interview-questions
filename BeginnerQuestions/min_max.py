def find_min_max(lst):
    # initialize min and max variables with first element of list
    min_elem = lst[0]
    max_elem = lst[0]

    # loop through the list, updating min and max variables where necessary
    for elem in lst:
        if elem < min_elem:
            min_elem = elem
        if elem > max_elem:
            max_elem = elem

    # return the min and max elements
    return min_elem, max_elem

# example
lst = [23, 52, 11, 91, 102, 46, 8, 77]
min_elem, max_elem = find_min_max(lst)
print("Minimum element:", min_elem) # output is 8
print("Maximum element:", max_elem) # output is 102