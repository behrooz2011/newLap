print('Hello, world!')

def maxi(x):
  j=0
  for index,val in enumerate(x):
    j+=val
    print("this is val: {} and this is index: {}".format(val,index))
  return j
    
maxi([1,-2,3,10,6])
print(maxi([1,-2,3,10,6]))

def neww(x):
  return maxi([1,-2,3,10,6])*x
print(neww(100))



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