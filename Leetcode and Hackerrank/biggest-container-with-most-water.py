def maxContainer(x):
  arr=[]
  for index,value in enumerate(x):
    for elem in range(index+1,len(x)):
      z=min(value,x[elem]) * (elem-index)
      arr.append(z)
  return max(arr)

print(maxContainer([1,9,3,5,10]))
print(maxContainer([1,8,6,2,5,4,8,3,7]))
print(maxContainer([1,1]))
print(maxContainer([4,3,2,1,4])) 


#better time complexity - o(n)
# Python3 code for Max 
# Water Container
def maxArea( A):
    l = 0
    r = len(A) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(A[l], 
                        A[r]) * (r - l))
     
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area
 
# Driver code
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]
 
print(maxArea(a))
print(maxArea(b))