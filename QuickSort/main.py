# swap two elements in `list_name`
def swap(list_name, i, j):
    list_name[i], list_name[j] = list_name[j], list_name[i]


def partition(list_name, start, end):
    pivot = list_name[end]  # set rightmost element as a pivot
    i = start - 1

    for j in range(start, end):
        if list_name[j] <= pivot:
            i += 1
            swap(list_name, i, j)
    swap(list_name, i + 1, end)
    return i + 1


# suppose we want ascending ordered list
def quickSort(list_name, start, end):
    if start < end:
        pivot = partition(list_name, start, end)

        quickSort(list_name, start, pivot-1)
        quickSort(list_name, pivot + 1, end)
    return list_name


# examples and expected results
example1 = [5, 3, 11, 8, 7]
result1 = [3, 5, 7, 8, 11]

example2 = [2, 9, 10, 11, 5, 3, 1]
result2 = [1, 2, 3, 5, 9, 10, 11]

example3 = [11, 9, 2, 0, 5, 6, 1, 8, 10, 3, 7, 4, 12]
result3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

example4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# if it returns False, it raises Assertion Error
# if it returns True, nothing happens
if __name__ == "__main__":
    assert quickSort(example1, 0, len(example1) - 1) == result1
    assert quickSort(example2, 0, len(example2) - 1) == result2
    assert quickSort(example3, 0, len(example3) - 1) == result3
    assert quickSort(example4, 0, len(example4) - 1) == result4
