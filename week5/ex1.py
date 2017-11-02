import os, time

pid = os.getpid()

while True:
   print(pid, time.time())
   time.sleep(2)