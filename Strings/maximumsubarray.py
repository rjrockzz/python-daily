  # My approach : A simple array traversal and summations

# arr = [1,4,3,5,6]
# x_sum = 12

# for x in range(len(arr)-1):
#     sum = arr[x]
#     for y in range(x+1,len(arr)):
#         sum = sum + arr[y]
#         if sum==x_sum:
#             print('{} {}'.format(x,y))

# Same Approach deals with test cases.

# Approach 2 : Assumption if elements of the are positive.
# if a subarray has a sum greater than the given sum
# start deleting the first elements

arr = [1,4,3,5,7]
x_sum = 8

def max_sum_arr(arr, x_sum):
    for i in range(len(arr)-1):
        sum = arr[i]
        for j in range(i+1, len(arr)):
            sum = sum + arr[j]
            l = 0
            if sum == x_sum:
                print('{} {}'.format(l, j))
            if sum > x_sum:    
                while sum!= x_sum:
                    sum = sum - arr[l]
                    l +=1
                print('{} {}'.format(l,j))
                return 1

max_sum_arr(arr, x_sum)