#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(1) when only adding to lists. O(n) when looping through recursively
    TODO: Memory usage: O(1) """
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    new_sorted_list = [] 

    # if both lists are empty 
    if not items1 and not items2:
      return new_sorted_list
    # if items1 is not empty but item2 is empty
    if items1 and not items2: 
      return new_sorted_list + items1
    # if items2 is not empty but item1 is empty
    if not items1 and items2: 
      return new_sorted_list + items2
    # if neither lists are empty
    if items1 and items2: 
      # if item in item1 is less than or equal to item in items2
      if items1[0] <= items2[0]:
        # append item in item1 to new_sorted_list
        new_sorted_list.append(items1[0])
        new_sorted_list += merge(items1[1:], items2) # recursive call until we reach the end of list
        print(new_sorted_list)
      # if item in item1 is greater than item in items2
      if items1[0] > items2[0]:
        # append item in item2 to new_sorted_list
        new_sorted_list.append(items2[0])
        new_sorted_list += merge(items1, items2[1:]) # recursive call until we reach the end of list
    return new_sorted_list



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n logn) for every case because we split the list everytime
    TODO: Memory usage: O(1) """

    # if list is empty  (Base case)
    if not items or len(items) <= 1:
      return items

    # TODO: Split items list into approximately equal halves
    mid = len(items)//2
    # start at index 0, end 1 indec before mid
    left = items[0:mid]
    # start at mid, end at the last index
    right = items[mid:]
    # Sort each half using any other sorting algorithm
    # Merge sorted halves into one list in sorted order
    return merge(split_sort_merge(left), split_sort_merge(right))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n logn) for every case
    TODO: Memory usage: O(1)"""
    # Check if list is so small it's already sorted (base case)
    if items == []:
        return items
    if len(items) == 1: #a list of 1 is already sorted
        return items

    # Split items list into approximately equal halves
    middle = len(items) // 2
    # gimmie the left chunk and the right chunk
    left = items[0:middle]
    right = items[middle:]

    # Sort each half by recursively calling merge sort
    resultleft = merge_sort(left)
    resultright = merge_sort(right)

    # Merge sorted halves into one list in sorted order
    return merge(resultleft, resultright)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (random pivot point) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n) looping over the range
    TODO: Memory usage: O(1) """

    # Choose a pivot using a built in random function
    random_index = random.randrange(low, high) # pivotal value

    # swap with items[high], we want the pivot value in the index where "high" values start (the end)
    items[high], items[random_index] = items[random_index], items[high]
    
    # We will start by checking the first item in the list
    pivot = low

    # Loop through all items in range [low...high]
    for i in range(low, high):
    # Move items less than pivot into front of range [low...p-1]
      if items[i] <= items[high]:
        items[i], items[pivot] = items[pivot], items[i]
        pivot += 1 
    # Move pivot item into final position [p] and return index p
    items[pivot], items[high] = items[high], items[pivot]
    return pivot


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n logn)=> simple partition or O(n)=> three-way partition and equal keys
    TODO: Worst case running time: O(n)^2 when pivot is constantly the greatest or the smallest number
    TODO: Memory usage: O(1) """
    # TODO: Check if high and low range bounds have default values (not given)
    # Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
      return items

    # Partition items in-place around a pivot and get index of pivot
    # Sort each sublist range by recursively calling quick sort
    if low < high: 
      pivot = partition(items, low, high)
      quick_sort(items, low, pivot - 1)
      quick_sort(items, pivot + 1, high)
    return items