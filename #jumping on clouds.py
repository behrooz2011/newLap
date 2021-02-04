#jumping on clouds
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def jumpingOnClouds(c):
    path=0
    i=0
    while i<len(c)-1:
        if i+2<len(c) and c[i+2]==0:
            path+=1
            i+=2
        elif i+1<len(c) and c[i+1]==0:
            path+=1
            i+=1
            
    return path