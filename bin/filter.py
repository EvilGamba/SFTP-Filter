from namelib import namelib
from guardlib import guard
from scriptlib import scripter
import sys , os , logging

def main():
    log = open(r"/etc/SFTP-Filter/history.log", 'a')
    filename = sys.argv[2]
    dir = sys.argv[1]
    path = dir + filename
    
    if not os.path.isfile(path):
        log.write("ERROR:  {0} is not a file Or Does not Exist\n".format(path))
        sys.exit("File Does Not Exist")
    
    namer = namelib()
    if not (namer.scan(filename)):
        log.write("INFO: {0} : Did Not Pass Name Rules Check\n".format(path))
        os.remove(path)
        log.write("INFO: {0} : Deleted from Server\n".format(path))
        sys.exit(0)
    log.write("INFO: {0} : Passed Name Check\n".format(path))
    
    sentry = guard()
    if not (sentry.scan(path)):
        log.write("INFO: {0} : Did Not Pass Security Check\n".format(path))
        os.remove(path)
        log.write("INFO: {0} : Deleted from Server\n".format(path))
        sys.exit(0)
    log.write("INFO: {0} : Passed Security Check\n".format(path))

    tinkerer = scripter()
    log.write("INFO: {0} : Goes Through Scripts\n".format(path))
    tinkerer.run_scripts(path)




if __name__ == '__main__':
    main()
