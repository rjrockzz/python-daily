'''
Selection Sort : Repeatedly find the minimum elements
1. We maintain 2 arrays :
    * The first sub array is already sorted
    * The second sub array is not sorted

- Best : O(n^2)
- Worst : O(n^2)
_ Average : O(n^2)
Summary :  Find the minimum element move to the sorted sub array.
'''


def selection_sort(arr):
    for i in range(len(arr) - 1): # 0 -> 7
        temp = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[temp]):
                temp = j
        if (temp != i):
            arr[i], arr[temp] = arr[temp], arr[i]
    return arr

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:',selection_sort(List))

