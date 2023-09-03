class ClassTableEntry:
    def __init__(self, name, inherits = "Object", size = 0):
        self.name = name
        self.inherits = inherits
        self.size = size
    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.inherits, self.size)

class ClassTable:
    def __init__(self, Entry = None):
        self.entries = []
        IOEntry = ClassTableEntry("IO", "Object")
        ObjectEntry = ClassTableEntry("Object", None)
        IntEntry = ClassTableEntry("Int", "Object")
        StringEntry = ClassTableEntry("String", "Object")
        BoolEntry = ClassTableEntry("Bool", "Object")
        self.entries.append(IOEntry)
        self.entries.append(ObjectEntry)
        self.entries.append(IntEntry)
        self.entries.append(StringEntry)
        self.entries.append(BoolEntry)
        if Entry:
            self.entries.append(Entry)

    def addEntry(self, Entry):
        if self.findEntry(Entry.name) is None:
            self.entries.append(Entry)
            return True
        else:
            return False

    def findEntry(self, name):
        for entry in self.entries:
            if entry.name == name:
                return entry
        return None