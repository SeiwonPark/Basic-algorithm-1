# suppose we want ascending ordered list
def mergeSort(list_name):
    if len(list_name) > 1:         # divide list until len(list_name) == 2
        mid = len(list_name) // 2
        left = list_name[:mid]     # divide list into two parts
        right = list_name[mid:]

        mergeSort(left)
        mergeSort(right)
        left_index, right_index, merged_index = 0, 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                list_name[merged_index] = right[right_index]
                right_index += 1
            else:
                list_name[merged_index] = left[left_index]
                left_index += 1
            merged_index += 1

        if left_index != len(left):
            list_name[merged_index:] = left[left_index:]
        else:
            list_name[merged_index:] = right[right_index:]
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
    assert mergeSort(example1) == result1
    assert mergeSort(example2) == result2
    assert mergeSort(example3) == result3
    assert mergeSort(example4) == result4
