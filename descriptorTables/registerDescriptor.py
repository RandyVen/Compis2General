from collections import namedtuple
from re import search

Register = namedtuple('Register', ['registerAdd', 'value'])
class RegisterDescriptor():
    def __init__(self) -> None:
        self.table = {
            "t0":[],
            "t1":[],
            "t2":[],
            "t3":[],
            "t4":[],
            "t5":[],
            "t6":[],
            "t7":[],
            "t8":[],
            "t9":[],
            "s0":[],
            "s1":[],
            "s2":[],
            "s3":[],
            "s4":[],
            "s5":[],
            "s6":[],
            "s7":[],
            "s8":[],
            "s9":[],
        }
    def getRegister(self, var) -> Register:
        checkingSize = 0
        while search:
            for key in self.table.keys():
                if len(self.table[key]) == checkingSize :
                    self.table[key].append(var)
                    if checkingSize == 0:
                        return Register(key, "empty")
                    else:
                        return Register(key, self.table[key][-1])
            checkingSize += 1
    
    def emptyRegister(self, reg:str) -> None:
        self.table[reg] = []

    def addValue(self, key, value):
        self.table[key].append(value)
 
    def __str__(self) -> str:
        strToReturn = ""
        for key in self.table.keys():
            toadd = key + ":"
            for item in self.table[key]:
                toadd += item + ","
            strToReturn += toadd + "\n"
        return strToReturn

        