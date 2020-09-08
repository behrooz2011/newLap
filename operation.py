#!/usr/bin/env python
import operator
import sys
import re

error={}
per_user={}
user={}
user_error={}

command = sys.argv[1]
with open(command)as f:
    for log in f:
        if re.search(r"Timeout while retrieving information",log) is not None:
            error["Timeout while retrieving information"]=error.get("Timeout while retrieving information",0)+1
            result1=re.search(r"\((w+)\)",log)
            user_error[result1[1]]=user_error.get([result1[1]],0)+1
        elif re.search(r"The ticket was modified while updating",log) is not None:
            error["The ticket was modified while updating"]=error.get("The ticket was modified while updating",0)+1
        elif re.search(r"Connection to DB failed",log) is not None:
            error["Connection to DB failed"]=error.get("Connection to DB failed",0)+1
        elif re.search(r"The ticket was modified while updating",log) is not None:
            error["The ticket was modified while updating"]=error.get("The ticket was modified while updating",0)+1
        elif re.search(r"Tried to add information to a closed ticket",log) is not None:
            error["Tried to add information to a closed ticket"]=error.get("Tried to add information to a closed ticket",0)+1
        elif re.search(r"Permission denied while closing ticket",log) is not None:
            error["Permission denied while closing ticket"]=error.get("Permission denied while closing ticket",0)+1
        elif re.search(r"Ticket doesn't exist",log) is not None:
            error["Ticket doesn't exist"]=error.get("Ticket doesn't exist",0)+1
        elif re.search(r"INFO",log) is not None:
            result=re.search(r"\((w+)\)",log)
            user[result[1]]=user.get([result[1]],0)+1
            
            per_user["Info Created"]=per_user.get("Info Created",0)+1
        elif re.search(r"INFO Commented",log) is not None:
            per_user["Info Commented"]=per_user.get("Info Commented",0)+1
        else:
            per_user["Info Closed"]=per_user.get("Info Closed",0)+1


sortedErr=sorted(error.items(), key = operator.itemgetter(1), reverse=True)
sorted.insert(0,("Error","Count"))
print(sortedErr)
print(error)
print(sorted(per_user.items(), key = operator.itemgetter(0), reverse=True))
  #####################################################################################
# import re
# import sys

# log="lets dance bye guys"
# # cc= sys.argv[1]
# count={}
# with open("operation_txt.txt")as f:
#     for line in f:
#         print(line.strip())



# #     count[x]=count.get(x,0)+1
# # print(count)



# # if re.search(r"hi",log) != None:
# #     print("hi founddddddddd")
# # elif re.search(r"by",log) != None:
# #     print(" good bye")
# # else:
# #     print("Not found")
###############################################################################

############## Solution #######################################################

#!/usr/bin/env python3
import re
import csv
import operator

error_messages = {}
per_user = {}
logfile =r"/home/<username>/syslog.log"
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

with open(logfile, "r") as f:
	for line in f:
		result = re.search(pattern, line)
		if result is None:
			continue
		if result.groups()[0] == "INFO":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':1, 'ERROR':0}
		if result.groups()[0] == "ERROR":
			category = result.groups()[0]
			message = result.groups()[1]
			name = str(result.groups()[2])[1:-1]
			error_messages[message] = error_messages.get(message, 0) + 1
			if name in per_user:
				user = per_user[name]
				user[category] += 1
			else:
				per_user[name] = {'INFO':0, 'ERROR':1}

sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
#sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = lambda x: x[1], reverse=True)
sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())[0:8]
#sorted_users = [("Username", "INFO", "ERROR")] + sorted(per_user.items())

with open("error_message.csv", "w") as error_file:
	for line in sorted_messages:
		error_file.write("{}, {}\n".format(line[0], line[1]))

with open("user_statistics.csv", "w") as user_file:
	for line in sorted_users:
		if isinstance(line[1], dict):
			user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
		else:
			user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))