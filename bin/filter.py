from namelib import namelib
from guardlib import guard
from scriptlib import scripter
import sys , os , logging

def main():
    log = open(r"/etc/SFTP-Filter/history.log", 'a')
    filename = sys.argv[2]
    dir = sys.argv[1]
    
    if not os.path.isfile(dir+filename):
        log.write("ERROR:  {0} is not a file Or Does not Exist\n".format(filename))
        sys.exit("File Does Not Exist")
    
    namer = namelib()
    if not (namer.scan(filename)):
        log.write("INFO: {0} : Did Not Pass Name Rules Check\n".format(filename))
        os.remove(filename)
        log.write("INFO: {0} : Deleted from Server\n".format(filename))
        sys.exit(0)
    log.write("INFO: {0} : Passed Name Check\n".format(filename))
    
    sentry = guard()
    if not (sentry.scan(filename)):
        log.write("INFO: {0} : Did Not Pass Security Check\n".format(filename))
        os.remove(filename)
        log.write("INFO: {0} : Deleted from Server\n".format(filename))
        sys.exit(0)
    log.write("INFO: {0} : Passed Security Check\n".format(filename))

    tinkerer = scripter()
    log.write("INFO: {0} : Goes Through Scripts\n".format(filename))
    tinkerer.run_scripts(filename)




if __name__ == '__main__':
    main()
