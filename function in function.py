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
