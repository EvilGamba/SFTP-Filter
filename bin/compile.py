# compiles all scripts made from compiled languages so they would not need to be compiled for every checked file
import json
import os


file = open(r"/etc/SFTP-Filter/scripts.json")
dic =json.load(file)
scripts = dic["compiled"]
location = r"/opt/SFTP_Filter/Compiled/Scripts/"
if not os.path.isdir(location):
    os.mkdir(location)
os.chdir(location)
for s in scripts:
    os.system("{0} {1} {2}".format(s["compiler"], s["location"], s["args"]))

