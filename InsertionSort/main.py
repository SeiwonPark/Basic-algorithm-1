# suppose we want ascending ordered list
def insertionSort(list_name):
    for i in range(1, len(list_name)):  # index starts from 1, since the list with one element is already sorted
        key = list_name[i]
        j = i - 1  # the largest element of the sorted group
        while j >= 0 and list_name[j] > key:
            list_name[j+1] = list_name[j]
            j -= 1
        list_name[j+1] = key
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
    assert insertionSort(example1) == result1
    assert insertionSort(example2) == result2
    assert insertionSort(example3) == result3
    assert insertionSort(example4) == result4
