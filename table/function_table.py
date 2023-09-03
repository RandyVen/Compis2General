


class FunctionTableEntry:
    def __init__(self,id ,name, type, scope = None,  belongsTo = None):
        self.id = id
        self.name = name
        self.type = type
        self.scope = scope
        self.belongsTo = belongsTo
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.id,self.name, self.type, self.scope, self.belongsTo)

class FunctionTable:
    def __init__(self):
        self.entries = []
        abort = FunctionTableEntry(1,"abort","Object", 1,"Object")
        type_name= FunctionTableEntry(2,"type_name","String", 1,"Object")
        copy = FunctionTableEntry(3,"copy","OBJECT", 1,"Object")
        out_string = FunctionTableEntry(4,"out_string","IO", 1,"IO")
        out_int = FunctionTableEntry(5,"out_int","IO", 1,"IO")
        in_string = FunctionTableEntry(6,"in_string","String", 1,"IO")
        in_int = FunctionTableEntry(7,"in_int","Int", 1,"IO")
        length = FunctionTableEntry(8,"length","Int", 1,"String")
        concat = FunctionTableEntry(9,"concat","String", 1,"String")
        substr = FunctionTableEntry(10,"substr","String", 1,"String")
        self.entries.append(abort)
        self.entries.append(type_name)
        self.entries.append(copy)
        self.entries.append(out_string)
        self.entries.append(out_int)
        self.entries.append(in_string)
        self.entries.append(in_int)
        self.entries.append(length)
        self.entries.append(concat)
        self.entries.append(substr)

    def addEntry(self, FunctionTableEntry):
        if self.findEntryByName(FunctionTableEntry.name, FunctionTableEntry.belongsTo) is None:
            self.entries.append(FunctionTableEntry)
            return True
        else:
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

