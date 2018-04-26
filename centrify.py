import subprocess

with open("/var/logs/HCLogs/lclog.txt","w") as f:
     try:
        cent=subprocess.check_output("rpm -qa | grep -i Centrify",shell=True)
        if cent != 1:
           f.write("Centrify is installed")
           f.write("\n")
           try:
              cent_status=subprocess.check_output("adinfo",shell=True)
              if cent != 1:
                 f.write("centrify is running")
              else:
                 f.write("centrify is not running")
           except:
             f.write("Centrify is not ruuning")
     except:
        f.write("centrify is not installed")
       
