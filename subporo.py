# import subprocess
# # subprocess.run(["date"])
# subprocess.run('date /t', shell=True)
# # subprocess.run(["sleep","2"])




############### Windows #############
# import subprocess
# result=subprocess.run(['date /t'], shell=True)
# print(result)

# import subprocess
# print(subprocess.run("date /t", shell=True))
# import subprocess
# print(subprocess.run('date/t', shell=True))

# import subprocess
# result=subprocess.run(["host","8.8.8.8"],capture_output=True)
# print(result)
# print(result.returncode)
import os
# print(os.environ)
print("this is the sep: \n",os.pathsep)
print(os.env)

