import os
import subprocess
import platform
opsname=platform.system()
def tanium_agent_check():
    '''Checks Whether Tanium  agent is installed or not'''
    if opsname=="Linux":
       tanium_check=subprocess.call('rpm -qa | grep -i Tanium TaniumClient-6.0.314.1442-1.x86_64',shell=True)
       if tanium_check==True:
          print("Tanium  agent is installed")
          def Tanium_status_check():
              ''''checks whether tanium agent is ruuning is ruuning or not'''
              if subprocess.call('ps -ef | grep -i tanium | grep -v grep',shell=True):
                 print("Tanium agent is running")
              else:
                 print("Tanium agent is not running")
          Tanium_status_check()
       else:
          print("Tanium agent is not installed")
    elif opsname=="Aix":
       tanium_check=subprocess.call('lslpp -l TaniumClient',shell=True)
       if tanium_check==True:
          print("Tanium agent is installed")
          Tanium_status_check()
       else:
          print("Tanium agent is not installed")
    elif opsname=="Solaris":
       tanium_check=subprocess.call('pkginfo -i TaniumClient',shell=True)
       if tanium_check==True:
          print("Tanium agent is installed")
          Tanium_status_check()
       else:
          print("Tanium agent is not installed")
tanium_agent_check()
