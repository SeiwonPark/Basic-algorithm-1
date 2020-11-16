# swap two elements in `list_name`
def swap(list_name, i, j):
    list_name[i], list_name[j] = list_name[j], list_name[i]


# 1. suppose we want max heap
#
def maxHeap(list_name, parent_index):
    temp = list_name[parent_index]

    while parent_index <= size // 2:
        child_index = parent_index * 2
        if child_index < size and list_name[child_index] < list_name[child_index + 1]:
            child_index += 1
        if temp > list_name[child_index]: break
        list_name[parent_index] = list_name[child_index]
        parent_index = child_index
    list_name[parent_index] = temp


def heapSort(list_name):
    global size
    size = len(list_name) - 1    # index of the last node
    for i in range(size//2, 0):
        maxHeap(list_name, i)

    while size > 1:
        swap(list_name, 0, size)
        size -= 1
        maxHeap(list_name, 0)

    return list_name

# 2. suppose we want min heap

# examples and expected results
example1 = [5, 3, 11, 8, 7]
result1 = [11, 8, 5, 3, 7]

example2 = [2, 9, 10, 11, 5, 3, 1]
result2 = [11, 10, 2, 9, 5, 3, 1]

example3 = [11, 9, 2, 0, 5, 6, 1, 8, 10, 3, 7, 4, 12]
result3 = [12, 10, 11, 9, 7, 2, 1, 8, 0, 3, 5, 4, 6]

example4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# if it returns False, it raises Assertion Error
# if it returns True, nothing happens
if __name__ == "__main__":
    assert heapSort(example1) == result1
    assert heapSort(example2) == result2
    assert heapSort(example3) == result3
    assert heapSort(example4) == result4