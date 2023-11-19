class VariableDescriptor():
    def __init__(self) -> None:
        self.table = {}
    
    def addVariableLocation(self,var:str, registry:str):
        if var in self.table.keys():
            self.table[var].append(registry)
        else:
            self.table[var] = []
            self.table[var].append(registry)
    
    def findLocationOfVar(self, var:str) -> str:
        if var in self.table.keys():
            return self.table[var][-1]
        else:
            return "mem"
    
    def __str__(self) -> str:
        strToReturn = ""
        for key in self.table.keys():
            toadd = key + ":"
            for item in self.table[key]:
                toadd += item + ","
            strToReturn += toadd + "\n"
        return strToReturn
