#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) where n is the number of elements in input array and k is the range of input
    Memory usage: O(n+k) """
    # FIXME: Improve this to mutate input instead of creating new output list
    # PSEUDOCODE:
    # Create temporary array to count each number count

    # Find range of given numbers (minimum and maximum integer values)
    numbers_length = len(numbers)
    k = max(numbers) + 1 

    # create a position list
    position = [0] * k

    # Create list of counts with a slot for each number in input range
    # increment values by 1
    for value in numbers: 
      position[value] += 1 

    #  Loop over given numbers and increment each number's count
    # iterate each index in position and track when a greater number is found
    counter = 0 
    for i in range(0, k): 
      temp = position[i]
      position[i] = counter
      counter += temp 

    # create output list by None 
    output = [None] * numbers_length

    # TODO: Loop over counts and append that many numbers into output list
    # place items directly into sorted position in result list based on info from position list 
    for value in numbers: 
      output[position[value]] = value
    #   position[value] += 1 

    return output

def bucket_sort(numbers):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n + k) for best case + average case, O(n^2) for worst case
    Memory usage: O(n + k)"""
    # FIXME: Improve this to mutate input instead of creating new output list
    # Find range of given numbers (minimum and maximum values)
    max_val = max(numbers)

    # Use the length of the list to figure out which value in the list goes in what bucket
    # DIVIDER to check which bucket the number should be placed
    size = max_val / len(numbers)


    # Create list of buckets to store numbers in subranges of input range
    bucket_list = []
    for x in range(len(numbers)):
        bucket_list.append([])

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        # figure out which bucket the current number should be in
        j = int(numbers[i] / size)
        if j != len (numbers):
            bucket_list[j].append(numbers[i])
        else:
            bucket_list[len(numbers) - 1].append(numbers[i])

    # Sort each bucket using any sorting algorithm (recursive or another)
    for z in range(len(numbers)):
        insertion_sort(bucket_list[z])

    # Loop over buckets and append each bucket's numbers into output list
    outputList = []
    for x in range(len(numbers)):
        outputList = outputList + bucket_list[x]
    return outputList
