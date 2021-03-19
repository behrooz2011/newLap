print('Hello, world!')
def twoSumNaive(num_arr, pair_sum):
  arr=[]
  # search first element in the array
  for i in range(len(num_arr)):
    # search other element in the array
    for j in range(i + 1, len(num_arr)):
      # if these two elemets sum to pair_sum, print the pair
      if num_arr[i] + num_arr[j] == pair_sum:
        arr.append([num_arr[i],num_arr[j]])
  print(arr)
      

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11,-1,6,1]
pair_sum = 7

# Function call inside print
twoSumNaive(num_arr, pair_sum) 

##########################################################
#TwoSum Unique pair finder
def twoSumUniq(arr,target):
  sum=[]
  obj={}
  for i in range(len(arr)):
    comp= target-arr[i]
    obj[arr[i]]=arr[i]
    if comp in obj:
      sum.append([comp,arr[i]])
      del obj[comp]
      del obj[arr[i]]
  print sum
twoSumUniq([4,8,5,8,5,5,5,7,3,6,6],9)
################################################

#TwoSum general

def twoSumHashing(num_arr, pair_sum):
    # sums = []
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
  
          hashTable[num_arr[i]] = num_arr[i]

# Driver Code
num_arr = [4, 5, 1, 8,5,5,5,7]
pair_sum = 9    
  
# Calling function
twoSumHashing(num_arr, pair_sum)


""" Repetitive"""
def twoS(x,target):
  obj={}
  sum=[]
  for i in range(len(x)):
    comp = target - x[i]
    obj[x[i]]= x[i]
    if comp in obj:
      sum.append([x[i],comp])
  return sum
print(twoS([4, 5, 1, 8,5,5,5,7],9))