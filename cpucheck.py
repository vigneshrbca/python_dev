import psutil

def cpu_check():
    cpu=psutil.cpu_percent()
    print(cpu)
cpu_check()
