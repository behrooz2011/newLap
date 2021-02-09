# print('Hello, world!')

def y(x):
    x.sort()
    dic={}
    for ozv in x:
        if ozv not in dic:
            dic[ozv]=1
            print("{} created".format(ozv))
        else:
            dic[ozv] += 1
    print(dic)
    mx=max(dic.values())
    for key,value in dic.items():
        if dic[key]==mx:
            return(key)


    
  
     
print(y([4,4,4,2,2,3,2,3,3,7,8,1]))
            