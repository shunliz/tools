import sys
import commands
import re

(status, output) = commands.getstatusoutput('docker images')

lines = re.split('\n', output)
lines = lines[1:-3]
for i in lines[:20]:
    results = re.split(r"\s+", i)
    (status, output) = commands.getstatusoutput("docker save "+results[0]+">images/"+results[2]+".tar")
