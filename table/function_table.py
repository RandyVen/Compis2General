class FunctionTable:
    def __init__(self):
        self.entries = []

    def addEntry(self, FunctionTableEntry):
        if self.findEntryByName(FunctionTableEntry.name, FunctionTableEntry.belongsTo) is None:
            self.entries.append(FunctionTableEntry)
        else:
            print("Function {0} already exists".format(FunctionTableEntry.name))
            return False

    def findEntryByName(self, name, belongsTo):
        for entry in self.entries:
            if entry.name == name and entry.belongsTo == belongsTo:
                return entry                
        return None
    def findEntryByID(self, id):
        for entry in self.entries:
            if entry.id == id:
                return entry
        return None

class FunctionTableEntry:
    def __init__(self,id ,name, type, scope = None,  belongsTo = None):
        self.id = id
        self.name = name
        self.scope = scope
        self.type = type
        self.belongsTo = belongsTo
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.id,self.name, self.type, self.scope, self.belongsTo)
