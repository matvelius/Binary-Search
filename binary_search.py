array = [0, 1, 3, 5, 7, 9, 12, 14, 19, 22, 25, 26, 47, 55]
target = 14


def binarySearch(array, target):

    if len(array) == 0:
        return -1
    
    midpoint = int(len(array) / 2)
    # print(midpoint)
    if array[midpoint] == target:
        print(midpoint)
        print(array[midpoint])
        return midpoint
    elif array[midpoint] < target:
        binarySearch(array[midpoint + 1:], target)
    elif array[midpoint] > target:
        binarySearch(array[:midpoint], target)
    else:
        return -1


binarySearch(array, target)