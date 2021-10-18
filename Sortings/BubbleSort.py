'''
Bubble Sort : just swap the adjacent elements and always
remember the last elements gets sorted first

- Best : 
- Worst : 
_ Average :
Summary :  Find the minimum element move to the sorted sub array.
'''
def bubbleSort(arr):
    for j in range(len(arr)- 1):
        for i in range(len(arr) - 1):
            if(arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


if __name__ == '__main__':
    arr = [1,5,2,4,6,2]
    print("The Sorted Array is : ", bubbleSort(arr))