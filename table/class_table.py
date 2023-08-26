class ClassTable:
    def __init__(self, ClassTableEntry = None):
        self.entries = []
        if ClassTableEntry:
            self.entries.append(ClassTableEntry)

    def addEntry(self, ClassTableEntry):
        if self.findEntry(ClassTableEntry.name) is None:
            self.entries.append(ClassTableEntry)
        else:
            print("Class {0} already exists".format(ClassTableEntry.name))
            return False

    def findEntry(self, name):
        for entry in self.entries:
            if entry.name == name:
                return entry
        return None
    
class ClassTableEntry:
    def __init__(self, name, inherits = None):
        self.name = name
        self.inherits = inherits
    def __str__(self):
        return '{0} {1}'.format(self.name, self.inherits)