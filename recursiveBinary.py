def find_item(list, item):
  #Returns True if the item is in the list, False if not.
    x=sorted(list)
    if len(list) == 0:
        return False

  #Is the item in the center of the list?
#   left=0
#   right=len(list)-1

#   while left<=right:
    middle = len(x)//2
    if x[middle] == item:
        return True

    #Is the item in the first half of the list? 
    if item < x[middle]:
        #Call the function with the first half of the list
        return find_item(x[:middle], item)
    else:
        #Call the function with the second half of the list
        return find_item(x[middle+1:], item)
    return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False