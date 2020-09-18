import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase 
  #and remove leading and trailing blanks
  st1 = string1.lower().strip()
  st2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,;:\-']"
  s1 = re.sub(punctuation, r"", st1)
  s2 = re.sub(punctuation, r"", st2)

  #DEBUG CODE GOES HERE
  # print("this is string1: '\n {} '\n and this is string2: '\n {}".format(string1,string2))

  return s1 == s2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False