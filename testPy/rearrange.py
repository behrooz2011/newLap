#!/usr/bin/env python3
import re

def rearrange_name(name):
    result = re.search(r"^([\w. ]*), ([\w. ]*)$",name)
    return "{} {}".format(result[2],result[1])

### here comes the manual test cases ###
print(rearrange_name("Glory, Joe"))
# print(rearrange_name("McCaine, Bob"))
# print(rearrange_name("...., boo.o"))
# print(rearrange_name("l..  ..l, lbo o.o"))
# print(rearrange_name("Marley, M Glen"))

# print(rearrange_name("Dario M, McCaine"))
