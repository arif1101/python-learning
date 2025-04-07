def LinearSearch(arr,targetValue):
    for i in range(len(arr)):
        if arr[i]==targetValue:
            return i+1
    return -1

arr = [3,7,2,9,5]
targetValue = 9
result = LinearSearch(arr,targetValue)
if(result == -1):
    print('values not found')
else:
    print(targetValue,'position is : ',result)