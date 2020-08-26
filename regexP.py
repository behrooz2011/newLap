# import re

# text = "123 this is not a really-big . or truly -fine algorithm"
# pattern = r"[0-9a-z]* [a-zA-Z]*"
# p2 = r"(\w*) (\w*) (\w*)-(\w*) \."

# res1= re.search(pattern,text)
# res2 = re.search(p2,text)

# print("this is res1 :\n",res1)
# print("this is res2: \n",res2)

# print("this is res2: \n",res2.groups())



import re
def show_time_of_pid(line):
  pattern = r"(\w*) (\w*) (\w*):(\w*):(\w*).*\[(\w*)\]"
  result = re.search(pattern, line)
  res = result.groups()

  return res[0]+' '+res[1]+ ' '+res[2]+':'+res[3]+':'+res[4]+' pid:'+res[5]
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

