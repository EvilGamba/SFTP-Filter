import json
import os
import logging

class scripter():
    __log = open("history.log", "a")
    __interpented = []
    __compiled = []
    __home = os.getcwd()
    def __init__(self) -> None:
        dic = json.load(open(r"/etc/SFTP-Filter/scripts.json","r"))
        inter = dic["interpented"]
        path = r"/opt/SFTP-Filter/Compiled/Scripts/"
        self.__interpented = self.__get_interpented(inter)
        self.__compiled = self.__get_Compiled(path)
    
    def __get_interpented(self,lst) -> list:
        # get all interpented scripts from json file
        interpented = []
        for dic in lst:
           interpented.append("{0} {1} {2}".format(dic["interpenter"], dic["location"], dic ["args"]))
        return interpented

    def __get_Compiled(self,path) -> list:
        # returns a list of the compiled
        relist = []
        if not os.path.isdir(path):
            #if the compiled scripts folder does not exists, there are not compiled scripts
            return []
        os.chdir(path)
        # work from the compiled scripts folder
        for subj in os.listdir(path):
            if os.path.isfile(subj):
                relist.append(os.path.abspath(subj))
        # return to the original working folder
        os.chdir(self.__home)
        return relist

    def run_scripts(self, path):
        # runs interpented scripts as long as the given file exists
        os.chdir(self.__home)
        for i in self.__interpented:
            if not os.path.exists(path):
                self.__log.write("INFO: {0} : Deleted by Script\n".format(path))
                return
            os.system("{0} {1}".format(i, path))
            self.__log.write("INFO: ran {0} on {1}\n".format(i , path))

        # runs scripts compiled by compile.py as long as the given file exists
        for c in self.__compiled:
            if not os.path.exists(path):
                return 
            os.system("{0} {1}".format(c, path)) 
            self.__log.write("INFO: ran {0} on {1}\n".format(c , path))
 