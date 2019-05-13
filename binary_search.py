array = [0, 1, 3, 5, 7, 9, 12, 14, 19, 22, 25, 26, 47, 55]
target = 3


def binarySearch(array, target):

    start = 0
    end = len(array) - 1

    if end == 0:
        return -1
    
    while start <= end:
        mid = int((start + end) / 2)

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

# def binarySearch(array, target):

#     start = 0
#     end = len(array) - 1
#     print(f"end: {end}")
#     # return -1

#     if end == 0:
#         print("array length is 0!")
#         return -1
    
#     while start <= end:
#         mid = int((start + end) / 2)
#         print(f"mid: {mid}")

#         if array[mid] == target:
#             print(f"found target! it's: {target}, at index: {mid}")
#             return mid
#         elif array[mid] < target:
#             print("array[mid] < target")
#             start = mid + 1
#             print(f"new start: {start}")
#         else:
#             print("array[mid] > target")
#             end = mid - 1
    
#     print("went thru the while loop, didn't find anything")

#     return -1

# recursive... but can't figure out how to return index!
# def binarySearch(array, target):

#     if len(array) == 0:
#         return -1
    
#     midpoint = int(len(array) / 2)
#     # print(midpoint)
#     if array[midpoint] == target:
#         print(midpoint)
#         print(array[midpoint])
#         return midpoint
#     elif array[midpoint] < target:
#         binarySearch(array[midpoint + 1:], target)
#     elif array[midpoint] > target:
#         binarySearch(array[:midpoint], target)
#     else:
#         return -1


binarySearch(array, target)