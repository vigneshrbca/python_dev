import psutil
with open('/tmp/sample.txt','wb') as f:
     cpu=psutil.cpu_percent()
     mem=psutil.virtual_memory().percent
     a="cpu:{}".format(cpu)
     b="mem:{}".format(mem)
     c=a+"|"+b
     f.write(c)


      
