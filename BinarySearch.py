def BinarySearch(arr, targetVal):
    left = 0
    right = len(arr) -1

    while(left <=right):
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return mid+1
        elif arr[mid] < targetVal:
            left = mid +1
        else:
            right = mid -1
    return -1

arr = [1,3,5,7,9,11,13,15,17,19,21]
targetVal = 3
result = BinarySearch(arr, targetVal)
if result==-1:
    print('not found');
else:
    print(result);