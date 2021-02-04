#finding the pairs
#There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example


# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

# Constraints

#  where 
# Sample Input

# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result={}
    for x in ar:
        if x not in result:
            result[x]=0
        result[x]+=1
    summ=0
    for key,value in result.items():
        summ+=value//2
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
