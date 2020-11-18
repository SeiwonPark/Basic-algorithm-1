# to do binary search, the given data should be already sorted
def binarySearch(arr, value):
    while len(arr) > 1:
        mid = len(arr) // 2
        if value < arr[mid]:
            arr = arr[:mid]
        else:
            arr = arr[mid:]

    if arr[0] == value:
        return True
    else:
        return False


# or just simply,
# def binarySearch(arr, value):
#     if value in arr:    # and in this case, arr doesn't need to be ordered already
#         return True
#     else:
#         return False

# examples and expected results
example1 = [3, 5, 7, 8, 11]
example2 = [1, 2, 3, 5, 9, 10, 11]
example3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
example4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    assert binarySearch(example1, 3) == True
    assert binarySearch(example2, 6) == False
    assert binarySearch(example3, 9) == True
    assert binarySearch(example4, 12) == False