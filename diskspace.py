import subprocess

threshold=90
partition="/"
df=subprocess.Popen(["df","-h"],stdout=subprocess.PIPE)
for line in df.stdout:
    splitline=line.split()
    print(splitline)
    #print(splitline[5])
    if splitline[5]==partition:
       disk_percent=int(splitline[4][:-1])
       #print(disk_percent)
