import psutil
def cpu_utilization():
    cpu=psutil.cpu_percent()
    print(cpu)
cpu_utilization()










