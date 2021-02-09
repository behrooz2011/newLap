print('Hello, world!')

def distance(x,z):
    x.sort()
    z.sort()
    newList=[]
    newList.append(x[0])
    for i,ozv in enumerate(x):
        if i!= 0:
            y=x[i]-x[i-1]
            newList.append(y)
            
        
    
    newList2=[]
    newList2.append(z[0])
    for j,oz in enumerate(z):
        if i!= 0:
            yy=z[j]-z[j-1]  
            newList2.append(yy)
    return max(newList)*max(newList2)
    
print(distance([1,6,3,7,11],[3,1]))
    

# def maxArea(h,w,hor,ver):
    