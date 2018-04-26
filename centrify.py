import subprocess
cent=subprocess.check_output("rpm -qa | grep -i Centrify",shell=True)
print(cent)
print("centrify is installed")
cent_status= subprocess.call("adinfo",shell=True)   
          
