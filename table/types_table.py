class TypesTable:
    def __init__(self):
        self.entries = ["Int", "Bool", "String", "Void"]
    
    def addEntry(self, type):
        self.entries.append(type)
    
    # finds type in table
    def findEntry(self, type):
        for entry in self.entries:
            if entry == type:
                return entry
        return None