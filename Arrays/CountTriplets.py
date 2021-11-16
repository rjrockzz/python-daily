# # Approach : Sort the array.
# # take three pointer variables
# # where i is the last
# # k is at i-1 place
# # j is at the starting

def triplet(arr,len):
    #Step 1
    arr.sort()
    n = len
    i = n-1
    count = 0
    while i>=0:
        j = 0
        k = i-1
        if(arr[i]== arr[j] + arr[k]):
           # print('{} {} {}'.format(arr[i],arr[j],arr[k]))
            count+=1
        elif arr[i] > arr[j]+arr[k]:
            j+=1
        else:
            k-=1
        i-=1
    print(count)
arr = [1,4,3,5,3,2,1,2]
len = len(arr)
triplet(arr,len)


# class Solution:
# 	def countTriplet(self, arr, n):
# 		self.arr = arr
# 		self.n = n
# 		arr.sort()
# 		count = 0
# 		i = n-1
# 		while i>=0:
# 		    k = i-1
# 		    j = 0
# 		    if arr[i]==arr[k]+arr[j]:
# 		        count+=1
# 		    elif arr[i]<arr[k]+arr[j]:
# 		        j+=1
# 		    else:
# 		        k-=1
# 		    i-=1
#             return count   
# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# if __name__ == '__main__':
# 	T=int(input())
# 	for i in range(T):
# 		n = int(input())
# 		arr = [int(x) for x in input().split()]

# 		ob = Solution()
# 		ans = ob.countTriplet(arr, n)
# 		print(ans)