from datetime import timedelta

with open('/proc/uptime','r') as fobj:
      uptime_seconds=float(fobj.readline().split()[0])
      uptime_string=str(timedelta(seconds=uptime_seconds))      
print(uptime_string)
