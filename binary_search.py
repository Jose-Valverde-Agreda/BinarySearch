import random
import time

# we are going to assume that the list given is in ascending order.

def naive_search(list_given, target):
    # target is the element that we are agoint to find
    for i in range(len(list_given)):
        if list_given[i] == target:
            return i
    # if we didn0t find the target, we'll return -1
    return -1



def binary_search(list_given, target, lower_limit=None, upper_limit=None):
    # The possible answer is a position. So we set the limits of that position
    if lower_limit == None:
        lower_limit = 0
    if upper_limit == None:
        upper_limit = len(list_given) -1
    if upper_limit < lower_limit:
        return -1
    # We are going to find the indice located in the middle
    mid_point = (lower_limit + upper_limit)//2
    if list_given[mid_point] == target:
        return mid_point
    elif target < list_given[mid_point]:
        return binary_search(list_given, target, lower_limit, mid_point-1)
    elif target > list_given[mid_point]:
        return binary_search(list_given, target, mid_point + 1, upper_limit)


if __name__ == '__main__':
    # create a list 
    size = 10000
    initial_set = set()
    while len(initial_set) < size:
        initial_set.add(random.randint(-3*size, 3*size)) 
    my_list = sorted(list(initial_set))
    # naive search
    ini = time.time()
    for element in my_list:
        naive_search(my_list, element)
    end = time.time()
    print(f"The time of naive search is : {end - ini} seconds")
    # binary search
    ini = time.time()
    for element in my_list:
        binary_search(my_list, element)
    end = time.time()
    print(f"The time of binary search is : {end - ini} seconds")