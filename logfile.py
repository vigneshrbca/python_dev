import datetime
import logging
import os


now=datetime.datetime.now()

def createlog(debuglevel):
      '''Creating Log File'''
      HealthCheckDirectory='/varlog/HC/HClog'

      if not os.path.exists(HealthCheckDirectory):
             os.makedirs(HealthCheckDirectory)
      logFileName=HealthCheckDirectory+'/'+now.isoformat()+'.log'
      logFileName=logFileName.replace('.','-')
      logFileName=logFileName.replace(':','-')
      if debuglevel=='':
         logLevel=logging.WARNING
      else:
         logLevel=logging.DEBUG
      logging.basicConfig(filename=logFileName,level=logLevel,format='%(asctime)s %(message)s')
      logging.warning('HealthCheck Log Starts')
      return logging;

#createlog('')

      
