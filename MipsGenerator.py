from intermediateCode.structures import Quadruple
import re
from descriptorTables.registerDescriptor import RegisterDescriptor
from descriptorTables.variableDescriptor import VariableDescriptor


class MipsGenerator():
    def __init__(self, intermediateCode:list, sizeOfMain:int):
        self.intermediateCode = intermediateCode
        self.sizeOfMain = sizeOfMain
        self.mipsCode = []
        self.registerDescriptorStack = [RegisterDescriptor()]
        self.variableDescriptorStack = [VariableDescriptor()]
        self.temporalPatern = re.compile(r't[0-9]*')

    def checkIfArgumentIsTemporal(self,arg):
        result = self.temporalPatern.match(arg)
        if result and result.group(0) == arg:
            return True
        return False

    def getOffsetOfVariables(self, addr: str):
        start = addr.index('[') + 1
        end = addr.index(']')
        return addr[start:end] 

    def generateMipsCode(self):
        mipsCode = ["addi $sp, $sp, -{0}".format(self.sizeOfMain), "jal mainMain"]
        for quadruple in self.intermediateCode:
            #Base case the code is a label no need to check anything else
            if quadruple.opp == "label":
                mipsCode.append("{0}:".format(quadruple.arg1))
                continue
            if quadruple.opp == "goto":
                mipsCode.append("   j {0}".format(quadruple.arg1))
                continue
            resultLocation = ''
            arg1Location = ''
            arg2Location = ''
            #Check if the result is stored in memory
            if (quadruple.result != None):

                print("I PASSED WHAT IS THE RESULT OF THIS ${quadruple.result}" + quadruple.result)

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
                    mipsCode.append("   mult ${}, {}, {}".format(resultLocation, arg1Location, arg2Location))
                elif quadruple.opp == "-":
                    mipsCode.append("   sub ${}, {}, {}".format(resultLocation, arg1Location, arg2Location))
                elif quadruple.opp == "=":
                    if resultLocation == "mem":
                        if not self.checkIfArgumentIsTemporal(arg1Location):
                            number = arg1Location
                            arg1Location = "$"+self.registerDescriptorStack[-1].getRegister(arg1Location).registerAdd
                            mipsCode.append("   add {}, {}, {}".format(arg1Location, arg1Location, number))
                        mipsCode.append("   sw {}, {}($sp)".format(arg1Location, self.getOffsetOfVariables(quadruple.result)))
                        self.variableDescriptorStack[-1].addVariableLocation(quadruple.result, arg1Location[1:])
                    else:
                        mipsCode.append("   add ${}, {}, $zero".format(resultLocation, arg1Location))
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
