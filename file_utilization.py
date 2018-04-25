import subprocess

a=subprocess.call('du /'.split()).split("\n")
print(a)


