print("hello dude!")
import subprocess
result=subprocess.run('date /t', shell=True,capture_output=True)
print(result.stdout)
print(result.stdout.decode())
print(result.returncode)