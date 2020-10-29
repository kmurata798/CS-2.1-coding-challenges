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
    # Repeat until all items are in sorted order

    # loop through each number
    for i in range(len(items):
        for j in range(len(items) - 1):
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
