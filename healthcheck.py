import socket
import platform
import psutil
import subprocess
import os

from logfile import createlog

opsname=platform.system()
currentlog=createlog('')

def general_info():
           '''Gives general information of server'''
           currentlog.warning('Server Information')
           try:
              hostname=socket.gethostname()
              hostip=socket.gethostbyname(hostname)
              osname=platform.system()
              osinfo=platform.dist()
              ostype=osinfo[0]
              osversion=osinfo[1]
              uptime=subprocess.check_output("uptime",shell=True)      
              currentlog.warning("HostName: {}".format(hostname))
              currentlog.warning("IP Address:{} ".format(hostip))
              currentlog.warning("OS Name:{}".format(osname))
              currentlog.warning("os Type:{}".format(ostype))
              currentlog.warning("os version:{}".format(osversion))
              currentlog.warning("uptime:{}".format(uptime))
           except:
              currentlog.warning("unable to get information")
 
def Cpu_utilization():
        '''Checks the Overall CPU Utilization of a server'''
        cpu=psutil.cpu_percent(interval=1)
        if cpu>90:
           currentlog.warning("cpu_utilization:{}".format(cpu))
           cpu_flag="RED"
           currentlog.warning("cpu_flag:{}".format(cpu_flag))
        elif cpu>80 and cpu<90:
           currentlog.warning("cpu_utilization:{}".format(cpu))
           cpu_flag="AMBER"
           currentlog.warning("cpu_flag:{}".format(cpu_flag))
        elif cpu<70:
           currentlog.warning("cpu_utilization:{}".format(cpu))
           cpu_flag="GREEN"
           currentlog.warning("cpu_flag:{}".format(cpu_flag))

def Memory_utilization():
        '''Gives the Memory utilization of a server'''
        mem=psutil.virtual_memory().percent
        if mem>90:
           currentlog.warning("Memory utilization:{}".format(mem))
           memory_flag="RED"
           currentlog.warning("memory_flag:{}".format(memory_flag))
        elif mem>80 and mem<90:
           currentlog.warning("Memory utilization:{}".format(mem))
           memory_flag="AMBER"
           currentlog.warning("memory_flag:{}".format(memory_flag))
        elif mem<70:
           currentlog.warning("Memory utilization:{}".format(mem))
           memory_flag="GREEN"
           currentlog.warning("memory_flag:{}".format(memory_flag))

def Disk_utilization():
        '''Gives the Disk utilization of a server in percent'''
        st=os.statvfs("/")
        free=(st.f_bavail*st.f_frsize)
        total=(st.f_blocks*st.f_frsize)
        used=(st.f_blocks-st.f_bfree)*st.f_frsize
        percent=(float(used)/total)*100
        if percent>90:
           currentlog.warning("Disk utilization:{}".format(percent))
           disk_flag="RED"
           currentlog.warning("Disk_flag:{}".format(disk_flag))
        elif percent>80 and percent<90:
           currentlog.warning("Disk utilization:{}".format(percent))
           disk_flag="AMBER"
           currentlog.warning("Disk_flag:{}".format(disk_flag))
        elif percent<70:
           currentlog.warning("Disk utilization:{}".format(percent))
           disk_flag="GREEN"
           currentlog.warning("Disk_flag:{}".format(disk_flag))
        
def list_running_process():
    '''Lists all the running process in the system'''
    for proc in psutil.process_iter(attrs=['pid','name','username']):
        currentlog.warning("Running Process in the server:{}".format(proc.info))
         
def splunk_agent_dir_check():
    '''Checks whether splunk is installed or not'''
    splunk_dir=os.path.isdir('/opt/splunkforwarder')
    if splunk_dir==True:
       currentlog.warning("Splunk agent is installed")
       def splunk_agent_check():
           '''Checks whether splunk agent is running or not'''
           if subprocess.check_output('ps -ef | grep splunkd | grep -v grep',shell=True):
             currentlog.warning("Splunk agent is running")
           else:
              currentlog.warning("splink agent is not running")
       splunk_agent_check()
    else:
       currentlog.warning("splunk agent is not installed")

def salt_stack_status_check():
    '''checks whether salt stack agent is running or not'''
    if subprocess.check_output('ps -ef | grep -i salt | grep -v grep',shell=True):
       currentlog.warning("salt stack agent is running")
    else:
       currentlog.warning("salt stack agent is not running") 


def salt_stack_agent_check():
    '''Checks Whether salt stack agent is installed or not'''
    if opsname=="Linux":
       salt_check=subprocess.check_output('rpm -qa | grep -i salt-m*',shell=True)
       if salt_check:
          currentlog.warning("Salt stack agent is installed")
          salt_stack_status_check()
       else: 
          currentlog.warning("salt stack agent is not installed")
    elif opsname=="AIX":
       salt_check=subprocess.check_output('lslpp -l salt.rte',shell=True)
       if salt_check:
          currentlog.warning("salt stack agent is installed")
          salt_stack_status_check()
       else:
          currentlog.warning("salt stack agent is not installed")
    elif opsname=="SunOS":
       salt_check=subprocess.check_output('pkginfo -i salt',shell=True)
       if salt_check:
          currentlog.warning("salt stack agent is installed")
          salt_stack_status_check()
       else:
          currentlog.warning("salt stack agent is not installed")

def Tanium_status_check():
    '''checks whether Tanium agent is running or not'''
    if subprocess.call('ps -ef | grep -i tanium | grep -v grep',shell=True):
       currentlog.warning("Tanium agent is running")
    else:
       currentlog.warning("Tanium agent is not running")


def tanium_agent_check():
    '''Checks Whether Tanium  agent is installed or not'''
    if opsname=="Linux":
       tanium_check=subprocess.call('rpm -qa | grep -i Tanium',shell=True)
       if tanium_check:
          currentlog.warning("Tanium  agent is installed")
          Tanium_status_check()
       else:
          currentlog.warning("Tanium agent is not installed")
    elif opsname=="AIX":
       tanium_check=subprocess.call('lslpp -l TaniumClient',shell=True)
       if tanium_check:
          currentlog.warning("Tanium agent is installed")
          Tanium_status_check()
       else:
          currentlog.warning("Tanium agent is not installed")
    elif opsname=="SunOS":
       tanium_check=subprocess.call('pkginfo -i TaniumClient',shell=True)
       if tanium_check:
          currentlog.warning("Tanium agent is installed")
          Tanium_status_check()
       else:
          currentlog.warning("Tanium agent is not installed")

def sysedge_agent_check():
    '''checks whether systemedge agent is installed or not'''
    sys_dir=os.path.isdir('/opt/CA/SystemEDGE')
    if sys_dir==True:
       currentlog.warning("SysEdge agent is installed")
       def sysedge_agent_status_check():
           '''Checks Whether Sysedge agent is installed or not'''
           if subprocess.check_output('ps -ef | grep -i Sysedge | grep -v grep',shell=True):
              currentlog.warning("Sysedge agent is running")
           else:
              currentlog.warning("Sysedge agent is not running")
       sysedge_agent_status_check()
    else:
       currentlog.warning("Sysedge agent is not installed") 

def linmon_check():
    '''checks whether linmon is installed or not'''
    if opsname=="Linux":
       lin_dir=os.path.isdir('/opt/admin/linmon')
       if lin_dir==True:
          currentlog.warning("linmon is installed")
          def linmon_status_check():
              '''checks whether linmon is running or not''' 
              if subprocess.check_output('ps -ef | grep -i linmon | grep -v grep',shell=True):
                 currentlog.warning("linmon is running")
              else:
                 currentlog.warning("linmon is not running")
          linmon_status_check()
       else:
          currentlog.warning("linmon is not installed") 

def sysmon_check():
    '''checks whether sysmon is installed or not'''
    if opsname=="AIX" or opsname=="SunOS":
       sys_file=os.path.isfile('/usr/local/etc/sysmon.rc')
       if sys_file==True:
          currentlog.warning("sysmon is installed")
          def sysmon_status_check():
              '''checks whether sysmon agent is running or not'''
              if subprocess.call('ps -ef | grep -i sysmon | grep -v grep',shell=True):
                 currentlog.warning("sysmon is running")
              else:
                 currentlog.warning("sysmon is not running")
          sysmon_status_check()
       else:
          currentlog.warning("sysmon is not installed")

def syslog_check():
    '''checks whether syslog is installed or not'''
    sys_file=os.path.isfile('/etc/*syslog.conf')
    if sys_file==True:
       currentlog.warning("syslog is installed")
       def syslog_status_check():
           '''checks whether syslog is running or not'''
           if subprocess.call('ps -ef | grep -i syslog | grep -v grep',shell=True):
              currentlog.warning("syslog is running")
           else:
              currentlog.warning("syslog is not running")
       syslog_status_check()
    else:
       currentlog.warning("syslog is not installed")

def ossec_agent_check():
    '''checks whether ossec agent is installed or not'''
    oss_file=os.path.isfile('/opt/ossec*/bin/ossec-agentd')
    if oss_file==True:
       currentlog.warning("ossec agent is installed")
       def ossec_agent_status_check():
           '''checks whether ossec_agent is running or not'''
           if subprocess.call('ps -ef | grep -i ossec | grep -v grep',shell=True):
              currentlog.warning("ossec agent is running")
           else:
              currentlog.warning("ossec agent is not running")
       ossec_agent_status_check()
    else:
       currentlog.warning("ossec agent is not installed")


def networker_agent_status_check():
    '''checks whether networker agent is running or not'''
    if subprocess.call('ps -ef | grep -i nsr | grep -v grep',shell=True):
       currentlog.warning("networker agent is running")
    else:
       currentlog.warning("networker agent is not running")


def networker_agent_check():
    '''checks whether networker agent is installed or not'''
    if opsname=="Linux":
       networker_check=subprocess.check_output('rpm -qa | grep -i LGTO',shell=True)
       if networker_check==True:
          currentlog.warning("networker agent is installed")
          networker_agent_status_check()
       else:
          currentlog.warning("networker agent is not installed")
    elif opsname=="AIX":
       networker_check=subprocess.check_output('lslpp -l | grep -i LGTO',shell=True)
       if networker_check:
          currentlog.warning("networker agent is installed")
          networker_agent_status_check()
       else:
          currentlog.warning("networker agent is not installed")
    elif opsname=="SunOS":
       networker_check=subprocess.check_output('pkginfo | grep -i LGTO',shell=True)
       if networker_check:
          currentlog.warning("networker agent is installed")
          networker_agent_status_check()
       else:
          currentlog.warning("networker agent is not installed")

def imperva_agent_check():
    '''checks whether imperva agent is installed or not'''
    imp_dir=os.path.isdir('/opt/imperva')
    if imp_dir==True:
       currentlog.warning("Imperva agent is installed")
       def imperva_agent_status_check():
           '''checks whether imperva agent is running or not'''
           if subprocess.call('ps -ef | grep -i imperva | grep -v grep',shell=True):
              currentlog.warning("Imperva agent is running")
           else:
              currentlog.warning("Imperva agent is not running")
       imperva_agent_status_check()
    else:
       currentlog.warning("Imperva agent is not installed")

def sendmail_agent_check():
    '''checks whether sendmail agent is installed or not'''
    smail=subprocess.call('rpm -qa | egrep -i sendmail',shell=True)
    if smail != 0:
       currentlog.warning("sendmail agent is installed")
       def sendmail_agent_status_check():
           '''check whether sendmail agent is running or not'''
           if subprocess.call('service sendmail status',shell=True):
              currentlog.warning("sendmail agent is running")
           else:
              currentlog.warning("sendmail agent is not running")
       sendmail_agent_status_check()
    else:
       currentlog.warning("sendmail agent is not installed")    

def vrops_agent_check():
    '''checks whether vrops agent is installed or not'''
    vop=subprocess.call('rpm -qa | grep -i epops-agent',shell=True)
    if vop !=0 :
       currentlog.warning("vrops agent is installed")
       def vrops_agent_status_check():
           '''checks whether vrops agent is running or not'''
           if subprocess.call('service epops-agent status',shell=True):
              currentlog.warning("vrops agent is running")
           else:
              currentlog.warning("vrops agent is not running")
       vrops_agent_status_check()
    else:
       currentlog.warning("vrops agent is installed")
 
def centrify_status_check():
    '''checks whether centrify agent is running or not'''
    if subprocess.call('adinfo',shell=True):
       currentlog.warning("centrify is running")
    else:
       currentlog.warning("centrify is not running")

def centrify_check():
    '''checks whether centrify is installed or not'''
    if opsname=="Linux":
       centrify_check=subprocess.call('rpm -qa | grep -i Centrify',shell=True)
       if centrify_check != True:
          currentlog.warning("centrify is installed")
          centrify_status_check()
       else:
          currentlog.warning("centrify is not installed")
    elif opsname=="AIX":
       centrify_check=subprocess.call('lslpp -l | grep -i centrify',shell=True)
       if centrify_check:
          currentlog.warning("centrify is installed")
          centrify_status_check()
       else:
          currentlog.warning("centrify is not installed")
    elif opsname=="SunOS":
       centrify_check=subprocess.call('Pkginfo | grep -i centry',shell=True)
       if centrify_check:
          currentlog.warning("centrify is installed")
          centrify_status_check()
       else:
          currentlog.warning("centrify is not installed")
     
    


           
general_info()
Cpu_utilization()
Memory_utilization()
Disk_utilization()
#list_running_process()
splunk_agent_dir_check()
salt_stack_agent_check()
tanium_agent_check()
sysedge_agent_check()
linmon_check()
sysmon_check()
syslog_check()
ossec_agent_check()
networker_agent_check()
imperva_agent_check()
sendmail_agent_check()
vrops_agent_check()
centrify_check()
