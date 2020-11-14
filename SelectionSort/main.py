# swap two elements in `list_name`
def swap(list_name, i, j):
    list_name[i], list_name[j] = list_name[j], list_name[i]


# suppose we want ascending ordered list
def selectionSort(list_name):
    for size in reversed(range(len(list_name))):
        maxValueIndex = 0
        for i in range(1, size + 1):
            if list_name[i] > list_name[maxValueIndex]:
                maxValueIndex = i
            swap(list_name, maxValueIndex, size)
    return list_name


# examples and expected results
example1 = [5, 3, 11, 8, 7]
result1 = [3, 5, 7, 8, 11]

example2 = [2, 9, 10, 11, 5, 3, 1]
result2 = [1, 2, 3, 5, 9, 10, 11]

example3 = [11, 9, 2, 0, 5, 6, 1, 8, 10, 3, 7, 4, 12]
result3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

example4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
result4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# if it returns False, it raises Assertion Error
# if it returns True, nothing happens
if __name__ == "__main__":
    assert selectionSort(example1) == result1
    assert selectionSort(example2) == result2
    assert selectionSort(example3) == result3
    assert selectionSort(example4) == result4
