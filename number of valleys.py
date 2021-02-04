#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def countingValleys(steps, path):
    li=list(path)
    print(li)
    valley=0
    sea1=0
    for index,value in enumerate(li):
        if li[index]=="U":
            sea1 += 1
        else:
            sea1 += -1
        if sea1 == 0 and li[index]=="U":
            valley+=1
    return valley
            