'''
Method 1 : Use a temporary array
Let's suppose an array : [1,2,3,4,5,6,7]
- provided d = 2, n = 7
temp [] = upto d elements : [1,2]
array + temp
will result in the array required

'''

def method_1(arr, d):
    temp = []
    for i in range(len(arr)):
        if i < d:
            temp.append(arr[0])
            arr.pop(0)
    final_array = arr + temp
    print("temp array : {} array : {} Final Array : {}".format(temp,arr,final_array))

method_1([1,2,3,4,5,6,7], 2)
