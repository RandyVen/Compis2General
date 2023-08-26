class AttributeTable:
    def __init__(self, AttributeTableEntry = None):
        self.entries = []
        if AttributeTableEntry:
            self.entries.append(AttributeTableEntry)
    
    def addEntry(self, AttributeTableEntry):
        if self.findEntry(AttributeTableEntry.name, AttributeTableEntry.type, AttributeTableEntry.scope, AttributeTableEntry.inClass, AttributeTableEntry.inMethod) is None:
            self.entries.append(AttributeTableEntry)
        else:
            print("Attribute {0} already exists".format(AttributeTableEntry.name))
            return False
    
    def findEntry(self, name, type, scope, inClass, inMethod):
        for entry in self.entries:
            if entry.name == name and entry.type == type and entry.scope == scope and entry.inClass == inClass and entry.inMethod == inMethod:
                return entry
            else:
                return None

class AttributeTableEntry:
    def __init__(self, name, type, scope = None, inClass = None, inMethod = None):
        self.name = name
        self.type = type
        self.scope = scope
        self.inClass = inClass
        self.inMethod = inMethod
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.name, self.type, self.scope, self.inClass, self.inMethod)