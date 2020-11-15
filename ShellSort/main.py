# bridging gaps
def gapInsertionSort(list_name, start, gap):
    for key in range(start+gap, len(list_name), gap):
        value = list_name[key]
        i = key
        while i > start:
            if list_name[i-gap] > value:
                list_name[i] = list_name[i-gap]
            else:
                break
            i -= gap
        list_name[i] = value


# suppose we want ascending ordered list
def shellSort(list_name):
    gap = len(list_name) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(list_name, start, gap)
        gap = gap // 2
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
    assert shellSort(example1) == result1
    assert shellSort(example2) == result2
    assert shellSort(example3) == result3
    assert shellSort(example4) == result4
