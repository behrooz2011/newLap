import re 
  
my_txt = "An investment in knowledge pays the best interest."
b="aroosak bozorge choobi"

def LetterCompiler(txt):
    result = re.findall(r'[a-c].', txt)
    return result
print(LetterCompiler(b))
print(LetterCompiler(my_txt))