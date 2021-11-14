  # My approach : A simple array traversal and summations

arr = [1,4,3,5,6]
x_sum = 12

for x in range(len(arr)-1):
    sum = arr[x]
    for y in range(x+1,len(arr)):
        sum = sum + arr[y]
        if sum==x_sum:
            print('{} {}'.format(x,y))

# Same Approach deals with test cases.

