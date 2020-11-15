# bridging gaps
def gapInsertionSort(list_name, start, gap):
    for key in range(start+gap, len(x), gap):
        value = list_name[key]
        i = key
        while i > start:
            if list_name[i-gap] > value:
                list_name[i] = list_name[i-gap]
            else:
                break
            i -= gap
        list_name[i] = value

def shellSort(list_name):
    gap = len(list_name) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(list_name, start, gap)
        gap = gap // 2
    return list_name
