import os
print("Trying to generate installer ")
from subprocess import call

my_env = os.environ.copy()
print(my_env["PATH"])
call([r'makeInstaller.bat'], env=my_env)