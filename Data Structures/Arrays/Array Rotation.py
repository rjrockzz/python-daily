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

'''
Method 2 : Rotating the array one by one
Let's define a function which could rotate an array by one and 
recursively call that function 
'''
def leftRotateByOne(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n-1):
        arr[i] = arr [i+1]
    arr[n-1] = temp

def letfRotate(arr,d):
    for i in range(d):
        leftRotateByOne(arr)

def printArray(arr):
    size = len(arr)
    for i in range(size):
        print ("% d"% arr[i], end =" ")

# main code
arr = [1,2,3,4,5,6,7,8]
letfRotate(arr,2)
printArray(arr)
