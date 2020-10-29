#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because we are using a loop to traverse through each item in the list
    Memory usage: O(1) because we aren't creating any additional data structures in the function"""
    # Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        current = items[i]
        nextItem = items[i + 1]
        if nextItem < current:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) because we are using a nested for loop to traverse through the list
    Memory usage: O(1) because we aren't creating any additional data structures in the function"""

    # loop through each index in the list
    # Repeat until all items are in sorted order
    for i in range(len(items):
        # loop through each index in the list while swapping adjacent  items
        for j in range(len(items) - 1):
            # check if current item is greater than the next item
            if items[j] > items[j+1]:
                # swap adjacent items that are out of order
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    O(n^2) because we are using a nested for loop to traverse through the list
    Memory usage: O(1) because we aren't creating any additional data structures in the function"""
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        # Find minimum item in unsorted items
        smallestIndex = i
        # loop through each UNSORTED item to find the next smallest number
        for j in range(i + 1, len(items) - 1):
            if items[j] < items[i]:
                smallestIndex = j
        # Swap it with first unsorted item
        items[i], items[smallestIndex] = items[smallestIndex], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) because we are using a while loop inside of a for loop
    TODO: Memory usage: O(1) because we aren't creating any additional data structures in the function"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    # loop through the list starting at index 1, since we will use index 0 to swap items
    for index in range(1, len(array)):
        # store the current itemValue in a variable
        currentValue = array[index]
        # and store the current itemIndex as well
        currentIndex = index

        # Loop through the list starting from the current item
        # The loop will continue until we reach the 0 index of the list,
        # (Since we are comparing/iterating from left to right when swapping)
        # And the loop must also check that the current item is less than the previous item
        while currentIndex > 0 and array[currentIndex - 1] > currentValue:
            # We set the current item to now equal the previous, greater item since we have a variable 
            # to keep track of the current item -> currentValue
            array[currentIndex] = array[currentIndex -1]
            # Set the currentIndex to be - 1 so that when the loop continues, we can compare the next two items in the list
            currentIndex -= 1


        # When the current item is at the 0 index, or the current item is greater than the item we are comparing it to,
        # we know that the item is now in the correct spot and we can make the swap
        # we're trying to insert at index currentIndex - 1.
        # Either way - we insert the element at currentIndex
        array[currentIndex] = currentValue
