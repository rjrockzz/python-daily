# Kadane's algorithm : Find the contigious sub-array 
# which has the maximum sum and return the sum.

# Greedy Approach #

# Python program to find maximum contiguous subarray
 
# Function to find the maximum contiguous subarray
# Kadane's algorithm : Find the contigious sub-array 
# which has the maximum sum and return the sum.

# Greedy Approach #

# Python program to find maximum contiguous subarray
 
# Function to find the maximum contiguous subarray
from sys import maxsize

def kadane(arr):
    max_so_far = -maxsize
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_so_far<max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here<0:
            max_ending_here = 0
    return max_so_far

arr = [-1,5,-6,-8,10,-5,30]
print(kadane(arr))

# Dynamic Approach

def maxSubArraySum(a,size):
    
    max_so_far =a[0]
    curr_max = a[0]
    
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
        
    return max_so_far

# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))
