# swap two elements in `list_name`
def swap(list_name, i, j):
    list_name[i], list_name[j] = list_name[j], list_name[i]


# 1. suppose we want max heap
def maxHeapify(list_name, parent_index):   # heapify in a max heap
    left_index = 2 * parent_index          # set left child index
    right_index = 2 * parent_index + 1     # set right child index
    if left_index != origin - 1 and right_index >= origin:
        return

    # in case there are two child nodes
    if left_index != origin - 1 and right_index > size:
        if list_name[left_index] > list_name[right_index] and list_name[left_index] > list_name[parent_index]:
            swap(list_name, left_index, parent_index)
        elif list_name[left_index] < list_name[right_index] and list_name[right_index] > list_name[parent_index]:
            swap(list_name, right_index, parent_index)

    # in case there's only left child
    elif left_index > size:
        if list_name[left_index] > list_name[parent_index]:
            swap(list_name, left_index, parent_index)

    maxHeapify(list_name, left_index)
    maxHeapify(list_name, right_index)


# 2. suppose we want min heap
def minHeapify(list_name, parent_index):   # heapify in a min heap
    left_index = 2 * parent_index          # set left child index
    right_index = 2 * parent_index + 1     # set right child index
    if left_index != origin - 1 and right_index >= origin:
        return

    # in case there are two child nodes
    if left_index != origin - 1 and right_index > size:
        if list_name[left_index] < list_name[right_index] and list_name[left_index] < list_name[parent_index]:
            swap(list_name, left_index, parent_index)
        elif list_name[left_index] > list_name[right_index] and list_name[right_index] < list_name[parent_index]:
            swap(list_name, right_index, parent_index)

    # in case there's only left child
    elif left_index >= size:
        if list_name[left_index] < list_name[parent_index]:
            swap(list_name, left_index, parent_index)

    minHeapify(list_name, left_index)
    minHeapify(list_name, right_index)


def maxHeapSort(list_name):   # move on steps to the root
    list_name.insert(0, 0)    # suppose index starts from '1'

    global size
    global origin
    origin = len(list_name)
    size = len(list_name) - 1    # index of the last node

    size //= 2
    while size != 0:
        maxHeapify(list_name, size)
        size -= 1

    del list_name[0]   # delete '0' which was inserted in #53

    return list_name


def minHeapSort(list_name):   # move on steps to the root
    list_name.insert(0, 0)    # suppose index starts from '1'

    global size
    global origin
    origin = len(list_name)
    size = len(list_name) - 1    # index of the last node

    size //= 2
    while size != 0:
        minHeapify(list_name, size)
        size -= 1

    del list_name[0]   # delete '0' which was inserted in #71

    return list_name


# examples and expected results
max_example1 = [5, 3, 11, 8, 7]
min_example1 = [5, 3, 11, 8, 7]
max_result1 = [11, 8, 5, 3, 7]
min_result1 = [3, 5, 11, 8, 7]
# example1 looks like this:
#             5
#            / \
#           3  11
#          / \
#         8  7
#
# max_result1 looks like this:
#             11            # In a max heap, root node has the largest value
#            / \
#           8   5           # In this max heap, parent always has larger value than those of children
#          / \
#         3  7
#
# min_result1 looks like this:
#             3             # In a min heap, root node has the smallest value
#            / \
#           5  11           # In this min heap, parent always has smaller value than those of children
#          / \
#         8  7

max_example2 = [2, 9, 10, 11, 5, 3, 1]
min_example2 = [2, 9, 10, 11, 5, 3, 1]
max_result2 = [11, 9, 10, 2, 5, 3, 1]
min_result2 = [1, 5, 2, 11, 9, 3, 10]

max_example3 = [11, 9, 2, 0, 5, 6, 1, 8, 10, 3, 7, 4, 12]
min_example3 = [11, 9, 2, 0, 5, 6, 1, 8, 10, 3, 7, 4, 12]
max_result3 = [12, 10, 11, 9, 7, 6, 1, 8, 0, 3, 5, 4, 2]
min_result3 = [0, 3, 1, 8, 5, 4, 2, 9, 10, 11, 7, 6, 12]

max_example4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
min_example4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
max_result4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
min_result4 = [1, 2, 4, 3, 6, 5, 8, 10, 7, 9]

max_example5 = [1, 16, 5, 30, 27, 17, 20, 2, 57, 3, 90]
min_example5 = [1, 16, 5, 30, 27, 17, 20, 2, 57, 3, 90]
max_result5 = [90, 57, 20, 30, 27, 17, 5, 2, 1, 3, 16]
min_result5 = [1, 2, 5, 16, 3, 17, 20, 30, 57, 27, 90]

# if it returns False, it raises Assertion Error
# if it returns True, nothing happens
if __name__ == "__main__":
    assert maxHeapSort(max_example1) == max_result1
    assert minHeapSort(min_example1) == min_result1
    assert maxHeapSort(max_example2) == max_result2
    assert minHeapSort(min_example2) == min_result2
    assert maxHeapSort(max_example3) == max_result3
    assert minHeapSort(min_example3) == min_result3
    assert maxHeapSort(max_example4) == max_result4
    assert minHeapSort(min_example4) == min_result4
    assert maxHeapSort(max_example5) == max_result5
    assert minHeapSort(min_example5) == min_result5