import psutil

cpu=psutil.cpu_percent(interval=1)
intensity=int(255*cpu/100)
print(intensity)
if intensity <  90:
   print("cpu_utilization:{}".format(intensity))
   status_flag="RED"
elif intensity > 80 and intensity < 90:
   print("cpu_utilization:{}".format(intensity))
   status_flag="AMBER"
elif intensity > 70:
   print("cpu_utilization:{}".format(intensity))


