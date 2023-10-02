class AttributeTableEntry:
    def __init__(self, name, type, scope = None, inClass = None, inMethod = None, isParam = False, size = 0, offset = 0):
        self.name = name
        self.type = type
        self.scope = scope
        self.inClass = inClass
        self.inMethod = inMethod
        self.isParam = isParam
        self.size = size
        self.offset = offset
    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.name, self.type, self.scope, self.inClass, self.inMethod, self.isParam, self.size, self.offset)


class AttributeTable:
    def __init__(self, Entry = None):
        self.entries = []
        outStringEntry = AttributeTableEntry("out_string", "String",2,"IO",4,True)
        outIntEntry = AttributeTableEntry("out_int", "Int",2,"IO",5,True)
        concatEntry = AttributeTableEntry("concat", "String",2,"String",9,True)
        susbstrEntry1 = AttributeTableEntry("start", "Int", 2,"String",10,True)
        susbstrEntry2 = AttributeTableEntry("End", "Int", 2,"String",10,True)
        self.entries.append(outStringEntry)
        self.entries.append(outIntEntry)
        self.entries.append(concatEntry)
        self.entries.append(susbstrEntry1)
        self.entries.append(susbstrEntry2)
        if Entry:
            self.entries.append(Entry)
    
    def addEntry(self, AttributeTableEntry):
        if self.findEntry(AttributeTableEntry.name, AttributeTableEntry.inClass, AttributeTableEntry.inMethod, AttributeTableEntry.scope) is None:
            self.entries.append(AttributeTableEntry)
            return True
        else:
            return False
    
    def findEntry(self, name, inClass, inMethod, scope):
        for entry in self.entries:
            if entry.name == name and entry.inClass == inClass and entry.inMethod == inMethod and entry.scope == scope:
                return entry
        return None
    
    def findParamsOfFunction(self, functionId):
        results = []
        for entry in self.entries:
            if entry.inMethod == functionId:
                if entry.isParam:
                    results.append(entry)
        return results
    
    def findLetsOffFunction(self, inMethod):
        results = []
        for entry in self.entries:
            if entry.inMethod == inMethod:
                if not entry.isParam:
                    results.append(entry)
        return results