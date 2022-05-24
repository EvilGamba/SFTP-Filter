import os
import json
import yara

def main():
    dic = {}
    i = 0
    dir = r"/opt/SFTP-Filter/YARA_Rules/"
    for path in os.listdir(dir):
        if path.endswith((".yara", ".yar")):
           dic["ruleset {}".format(i)] = dir+path
           i += 1
    rules = yara.compile(filepaths = dic)
    rules.save(r"Compiled_Rules") 




if __name__ == '__main__':
    main()