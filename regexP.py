import re

text = "123 this is not a really-big . or truly -fine algorithm"
pattern = r"[0-9a-z]* [a-zA-Z]*"
p2 = r"(\w*) (\w*) (\w*)-(\w*) \."

res1= re.search(pattern,text)
res2 = re.search(p2,text)

print("this is res1 :\n",res1)
print("this is res2: \n",res2)

print("this is res2: \n",res2.groups())
