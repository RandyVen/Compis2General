class ActivationRegister():
    def __init__(self, functionName = "Start") -> None:
        self.functionName = functionName
        self.registryInfo = {}
        self.size = 0
    
    def generateRegistryInfo(self, registerDescriptorTable):
        activationRegister = {}
        offset = 0
        size = 0
        for key in registerDescriptorTable.keys():
            currentKeyValue = registerDescriptorTable[key]
            if len(currentKeyValue) > 0:
                valueToSave = currentKeyValue[-1]
                size += 4
                activationRegister[key] = offset
                offset += 4
        self.registryInfo= activationRegister
        self.size = size