import os
import json
import yara

def main():
    dic = {}
    i = 0
    # set up working dir
    dir = r"/opt/SFTP-Filter/YARA_Rules/"
    for path in os.listdir(dir):
        if path.endswith((".yara", ".yar")):
            #for every yara rules file and to a dictionary (you have to unfortunatley) and use the dictionary to compile all files together
           dic["ruleset {}".format(i)] = dir+path
           i += 1
    rules = yara.compile(filepaths = dic)
    rules.save(r"Compiled_Rules") 




if __name__ == '__main__':
    main()
