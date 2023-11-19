from intermediateCode.structures import Quadruple
import re
from descriptorTables.registerDescriptor import RegisterDescriptor
from descriptorTables.variableDescriptor import VariableDescriptor
from descriptorTables.activationRegister import ActivationRegister


class MipsGenerator():
    def __init__(self, intermediateCode:list, sizeOfMain:int):
        self.intermediateCode = intermediateCode
        self.sizeOfMain = sizeOfMain
        self.mipsCode = []
        self.registerDescriptorStack = [RegisterDescriptor()]
        self.variableDescriptorStack = [VariableDescriptor()]
        self.activationRegisterStack = [ActivationRegister()]
        self.temporalPatern = re.compile(r't[0-9]*')
        self.functionSizes = {}
        self.getSizeOfFunctions()
        print(self.functionSizes)
        
    def searchActivationRegisterOfFunction(self, functionName):
        for i in self.activationRegisterStack:
            if i.functionName == functionName:
                return i
    
    def checkIfArgumentIsTemporal(self,arg):
        result = self.temporalPatern.match(arg)
        if result and result.group(0) == arg:
            return True
        return False

    def getOffsetOfVariables(self, addr: str):
        start = addr.index('[') + 1
        end = addr.index(']')
        return str(int(addr[start:end]) + 4) 

    def getSizeOfFunctions(self):
        lastAllocate = ""
        self.functionSizes["mainMain"] = self.sizeOfMain
        for quadruple in self.intermediateCode:
            if quadruple.opp == "allocate_in_stack":
                lastAllocate = quadruple.arg1 + 4
            if quadruple.opp == "call":
                self.functionSizes[quadruple.arg1] = lastAllocate
    
    def generateMipsCode(self):
        mipsCode = ["addi $sp, $sp, -{0}".format(self.sizeOfMain), "jal mainMain"]
        
        justCreatedObject = False
        currFunction = ""
        for quadruple in self.intermediateCode:
            #Base case the code is a label no need to check anything else
            if quadruple.opp == "label":
                mipsCode.append("{0}:".format(quadruple.arg1))
                if "IF" not in quadruple.arg1 and "Next" not in quadruple.arg1:
                    self.registerDescriptorStack.append(RegisterDescriptor())
                    self.variableDescriptorStack.append(VariableDescriptor())
                    self.activationRegisterStack.append(ActivationRegister(quadruple.arg1))
                    mipsCode.append("   sw $ra 0($sp)")
                    currFunction = quadruple.arg1
                continue
            if quadruple.opp == "goto":
                mipsCode.append("   j {0}".format(quadruple.arg1))
                continue
            if quadruple.opp == "allocate_in_stack":                
                mipsCode.append("   addi $sp, $sp, -{0}".format(quadruple.arg1+4))
                continue
            if quadruple.opp == "allocate_in_heap":
                mipsCode.append("   li $a0, {}".format(quadruple.arg1))
                mipsCode.append("   li $v0, 9")
                mipsCode.append("   syscall")
                justCreatedObject = True
                continue
            if quadruple.opp == "call":
                currentFunctionActivationRegister = self.searchActivationRegisterOfFunction(currFunction)
                #Save the current state of the machine
                currentFunctionActivationRegister.generateRegistryInfo(self.registerDescriptorStack[-1].table)
                mipsCode.append("   addi $sp, $sp , -{}".format(currentFunctionActivationRegister.size))
                for key in currentFunctionActivationRegister.registryInfo.keys():
                    mipsCode.append("   sw ${}, {}($sp)".format(key, currentFunctionActivationRegister.registryInfo[key]))
                #Return the stack to the area where params are stored
                mipsCode.append("   addi $sp, $sp , {}".format(currentFunctionActivationRegister.size))
                mipsCode.append("   jal {}".format(quadruple.arg1))
                mipsCode.append("   addi $sp, $sp , -{}".format(currentFunctionActivationRegister.size))
                for key in currentFunctionActivationRegister.registryInfo.keys():
                    mipsCode.append("   lw ${}, {}($sp)".format(key, currentFunctionActivationRegister.registryInfo[key]))
                mipsCode.append("   addi $sp, $sp, {}".format(currentFunctionActivationRegister.size))
                mipsCode.append("   addi $sp, $sp, {}".format(self.functionSizes[quadruple.arg1]))
                continue
            resultLocation = ''
            arg1Location = ''
            arg2Location = ''
            #Check if the result is stored in memory
            if "OBJECT_" in quadruple.result or "Function_" in quadruple.result:
                resultLocation = 'mem'
            #Check if the result is sotred in a temporary and "reserve" said temporal
            elif self.checkIfArgumentIsTemporal(quadruple.result):
                self.registerDescriptorStack[-1].addValue(quadruple.result, "temp")
                resultLocation = quadruple.result
            #Check if the result is to be stored in $v0
            elif "functionCallReturnAddr" in quadruple.result:
                resultLocation = "v0"
            #check if the result is a label (usefull for conditional branching)
            else:
                resultLocation = quadruple.result
            if quadruple.arg1:
                if self.checkIfArgumentIsTemporal(quadruple.arg1):
                    arg1Location = "$"+quadruple.arg1
                elif "OBJECT_Main" in quadruple.arg1 or "Function_" in quadruple.arg1:
                    if self.variableDescriptorStack[-1].findLocationOfVar(quadruple.arg1) == "mem":
                        register = self.registerDescriptorStack[-1].getRegister(quadruple.arg1)
                        self.variableDescriptorStack[-1].addVariableLocation(quadruple.arg1, register.registerAdd)
                        if register.value == "empty":
                            mipsCode.append("   lw ${0}, {1}($sp)".format(register.registerAdd, self.getOffsetOfVariables(quadruple.arg1)))
                        else:
                            pass
                        arg1Location = "$"+register.registerAdd
                    else:
                        arg1Location = "$"+self.variableDescriptorStack[-1].findLocationOfVar(quadruple.arg1)
                elif "functionCallReturnAddr" in quadruple.arg1:
                    arg1Location = "$v0"
                else:
                    if justCreatedObject:
                        arg1Location = "$v0"
                        justCreatedObject = False
                    else:
                        arg1Location = quadruple.arg1

            if quadruple.arg2:
                if self.checkIfArgumentIsTemporal(quadruple.arg2):
                    arg2Location = "$"+quadruple.arg2
                elif "OBJECT_Main" in quadruple.arg2 or "Function_" in quadruple.arg2:
                    if self.variableDescriptorStack[-1].findLocationOfVar(quadruple.arg2) == "mem":
                        register = self.registerDescriptorStack[-1].getRegister(quadruple.arg2)
                        self.variableDescriptorStack[-1].addVariableLocation(quadruple.arg2, register.registerAdd)
                        if register.value == "empty":
                            mipsCode.append("   lw ${0}, {1}($sp)".format(register.registerAdd, self.getOffsetOfVariables(quadruple.arg2)))
                        else:
                            pass
                        arg2Location = "$"+register.registerAdd
                    else:
                        arg2Location = "$"+self.variableDescriptorStack[-1].findLocationOfVar(quadruple.arg2)
                elif "functionCallReturnAddr" in quadruple.arg2:
                    arg2Location = "$v0"
                else:
                    arg2Location = quadruple.arg2
            
            #Add code related to operation
            if quadruple.opp == "+":
                mipsCode.append("   add ${}, {}, {}".format(resultLocation, arg1Location, arg2Location))
            elif quadruple.opp == "*":
                mipsCode.append("   mult {}, {}".format(arg1Location, arg2Location))
                mipsCode.append("   mflo ${}".format(resultLocation))

            elif quadruple.opp == "/":
                mipsCode.append("   div {}, {}".format(arg1Location, arg2Location))
                mipsCode.append("   mflo ${}".format(resultLocation))
            elif quadruple.opp == "-":
                mipsCode.append("   sub ${}, {}, {}".format(resultLocation, arg1Location, arg2Location))
            elif quadruple.opp == "=":
                if resultLocation == "mem":
                    if arg1Location == "$v0":
                        pass
                    elif '$' not in arg1Location and not self.checkIfArgumentIsTemporal(arg1Location)  :
                        
                        number = arg1Location
                        print(number)
                        arg1Location = "$"+self.registerDescriptorStack[-1].getRegister(arg1Location).registerAdd
                        mipsCode.append("   li {}, {}".format(arg1Location, number))

                    mipsCode.append("   sw {}, {}($sp)".format(arg1Location, self.getOffsetOfVariables(quadruple.result)))
                    self.variableDescriptorStack[-1].addVariableLocation(quadruple.result, arg1Location[1:])
                elif resultLocation == "v0":
                    if currFunction == "mainMain":
                        mipsCode.append("   li $v0, 10")
                        mipsCode.append("   syscall")
                    else:    
                        mipsCode.append("   add ${}, {}, $zero".format(resultLocation, arg1Location))
                        mipsCode.append("   lw $ra, 0($sp)")
                        mipsCode.append("   jr $ra")
                        self.registerDescriptorStack.pop()
                        self.variableDescriptorStack.pop()
                else:
                    mipsCode.append("   move ${}, {}".format(resultLocation, arg1Location))
            elif quadruple.opp == "<":
                mipsCode.append("   blt {}, {}, {}".format(arg1Location, arg2Location, resultLocation))
            elif quadruple.opp == "<=":
                mipsCode.append("   ble {}, {}, {}".format(arg1Location, arg2Location, resultLocation))
            elif quadruple.opp == "eq":
                mipsCode.append("   beq {}, {}, {}".format(arg1Location, arg2Location, resultLocation))
            

        self.mipsCode = mipsCode
    
    def __str__(self) -> str:
        result = ""
        for i in self.mipsCode:
            result += i + '\n'
        return result

if __name__ == "__main__":
    generator = MipsGenerator([])
