import yara
import json

class guard():
    __rules = None
    def __init__(self) -> None:
        self.__rules = yara.load(r"opt/Filtered-SFTP/Compiled_Rules")
        
    def scan(self, path) -> bool:
        matches = self.__rules.match(path)
        if len(matches) > 0:
            return False
        return True
        
            
