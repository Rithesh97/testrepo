import subprocess
import re
import os
import csv
header=True
count=1
biometric_status={}
os.chdir(r"C:\\Users\\ithd.gedbs\\Desktop\\")
with open("newbiometricdetails.csv") as file:
  rows=csv.reader(file)
  for row in rows :
    if header==True:
      header=False
      continue
    department,device_ip=row
    result=subprocess.run(["ping",device_ip,"-n","1"],capture_output=True)
    output=result.stdout.decode().split()
    if "unreachable." in  output:
      biometric_status[department]="Down"
    elif result.returncode==0:
      biometric_status[department]="UP"    
    else:
      biometric_status[department]="Not an Biometric Device or Invalid IP"
print(str(biometric_status).replace(',','\n'))  
input("Thank you")
