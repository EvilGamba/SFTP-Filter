import re
import codecs

class namelib():
    __rules = []
    def __init__(self):
        NAMERULES = r"/etc/SFTP-Filter/rules.txt"
        self.__rules = self.__reader(NAMERULES)
    def __reader(self, path : str):
        rules = []
        rulefile = open(path, 'r')
        for line in rulefile.readlines():
            flag = False
            words = line[:-1].split(' ')
            if words[0] == "NOT":
                flag = True
                words = words[1::]
            rules.append((words[0], words[1::], flag))
        rulefile.close()
        return rules

    def scan(self, subject: str) -> bool:
        # returns true if the filename fit all of the rules in the NAMERULES file
        subject = subject.split('/')[-1]
        for cmd, args, flag in self.__rules:
            if not self.__commander(cmd, args, subject, flag):
                return False
        return True

    def __commander(self, cmd: str, args: str, subject: str, flag: bool) -> bool:
        if flag:
            # For the Not Command
            return not self.__commander(cmd, args, subject, False)
        if cmd == "IS":
            return self.__fullname(subject, args)
        if cmd == "END":
            return self.__string_end(subject, args)
        if cmd == "CONTAIN_ONE":
            return self.__string_contain_one(subject, args)
        if cmd == "CONTAIN_ALL":
            return self.__string_contain_all(subject, args)
        if cmd == "REGEX":
            return self.__string_regex(subject, args)
        # else: ignore line

    def __string_contain_one(self, subject, args):
        # If contains one of the arguments return true
        for arg in args:
            if re.search(subject, arg):
                return True
        return False

    def __string_contain_all(self, subject, args):
        #if containes all of the arguemnt return true
        print (args)
        for arg in args:
            if arg not in subject:
                print (arg)
                return False
        return True

    def __fullname(self, subject, args):
        # checks if one of the arguments is the filename
        for arg in args:
            if subject == arg:
                return True
        return False

    def __string_end(self, subject, args):
        for arg in args:
            if subject.endswith(arg):
                return True
        return False

    def __string_regex(self, subject, args):
        pattern = args[0]
        codecs.decode(pattern, 'unicode_escape')
        if re.search(pattern, subject):
            return True
        return False
