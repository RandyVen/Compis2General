class AttributeTable:
    def __init__(self, AttributeTableEntry = None):
        self.entries = []
        if AttributeTableEntry:
            self.entries.append(AttributeTableEntry)
    
    def addEntry(self, AttributeTableEntry):
        self.entries.append(AttributeTableEntry)
    
    def findEntry(self, name, type, scope, belongsTo):
        for entry in self.entries:
            if entry.name == name and entry.type == type and entry.scope == scope and entry.belongsTo == belongsTo:
                return entry
            else:
                raise NameError("{0} Not declared in {1}".format(name,belongsTo))

class AttributeTableEntry:
    def __init__(self, name, type, scope, belongsTo) -> None:
        self.name = name
        self.type = type
        self.scope = scope
        self.belongsTo = belongsTo
