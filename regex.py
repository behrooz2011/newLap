import re
inp="this is Jan 31 13:02:29 in LA"
pattern = r"Jan (d+) (d{2}):(d{2}):(d{2})"
result = re.search(pattern,inp)
print(result)