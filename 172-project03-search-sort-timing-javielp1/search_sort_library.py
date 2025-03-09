
def is_sorted(a_list):
    """:return: True if number_list is sorted in ascending order, False otherwise"""
    for i in range(len(a_list)-1):
        if a_list[i] > a_list[i+1]:
            return False
    return True



def my_linear_search(a_list, item_to_find):
    """:return: an index of a place in a_list where an item_to_find is located, or -1 if not present"""
    # use your own searching code for this function
    for i in range(len(a_list)):
        if a_list[i] == item_to_find:
            return i
    return -1



def system_linear_search(a_list, item_to_find):
    """:return: an index of a place in a_list where an item_to_find is located, or -1 if not present"""
    # use a built-in function of python to search, no loop in your code
    try:
        return a_list.index(item_to_find)
    except ValueError:
        return -1



def my_sort(a_list):
    """:post: a_list is sorted least to greatest"""
    # use your own sorting algorithm for this problem
    l = len(a_list)
    for i in range(l):
        for j in range(0,l- i - 1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list





def system_sort(a_list):
    """:post: a_list is sorted least to greatest"""
    # use a built-in sorting function that is part of python, no loops
    a_list.sort()



def my_binary_search(a_list, item_to_find):
    """
        :pre: a_list must be sorted least to greatest
        :return: an index of a place in a_list where an item_to_find is located, or -1 if not present
    """
    min_index = 0
    max_index = len(a_list) -1
    while max_index >= min_index:
        mid = (max_index + min_index) // 2
        if a_list[mid] == item_to_find:
            return mid
        elif a_list[mid] < item_to_find:
            min_index = mid + 1
        else:
            max_index = mid - 1
    return -1



