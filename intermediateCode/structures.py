class Quadruple():
    def __init__(self, opp, arg1, result ,arg2 = None):
        self.opp = opp
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result
    
    def __str__(self) -> str:
            if self.opp == "=" :
                return "{0} {1} {2}".format(self.result, self.opp, self.arg1)
            if self.opp == "label":
                return "\n{0}:\n".format(self.arg1)
            if self.opp == "goto":
                return "{0} {1}".format(self.opp,self.arg1)
            if self.opp == "<" or self.opp == "<=" or self.opp == "eq":
                return "{0} {1} {2} {3}".format(self.arg1, self.opp, self.arg2, self.result)
            if self.opp =="allocate_in_stack" or self.opp =="allocate_in_heap":
                return "{0}[{1}]".format(self.opp, self.arg1)
            if self.opp == "call":
                return "{0} {1}".format(self.opp, self.arg1)
            if self.opp == "!=":
                return "{0} = not {1}".format(self.result, self.arg1)
            if self.opp == "void":
                return "{0} = isVoid {1}".format(self.result, self.arg1)
            if self.opp =="blank":
                return ""
            if self.arg2:
                return "{0} = {1} {2} {3}".format(self.result, self.arg1, self.opp, self.arg2)
            else:
                return "{0} = {1}{2}".format(self.result, self.opp, self.arg1)

class ProductionInformation():
    def __init__(self):
        self.addr = 't-1'
        self.true = "wut"
        self.false = "wut"
        self.next = "wut" 
        self.code = []

    def addCode(self, code: list):
        for line in code:
            self.code.append(line)
        
    def setAddr(self, addr:str):
        self.addr = addr

    def __str__(self):
        string = ''
        for line in self.code:
            string += str(line) + "\n"
        return string

class TemporalGenerator():
    def __init__(self):
        self.counter = 0

    def newTemporal(self):
        self.counter +=1
        return 't{}'.format(self.counter)

class LableGenerator():
    def __init__(self):
        self.ifCounter = 0
        self.whileCounter = 0
        self.nextCounter = 0

    def generateTrue(self,num) -> str:
        return "IF{0}True".format(num)

    def generateFalse(self,num) -> str:
        return "IF{0}False".format(num)
    
    def generateIfLabels(self) -> str:
        trueLabel, falseLabel = self.generateTrue(self.ifCounter), self.generateFalse(self.ifCounter)
        self.ifCounter += 1
        return trueLabel, falseLabel

    def generateNext(self) -> str:
        toReturn = "Next{0}".format(self.nextCounter)
        self.nextCounter += 1
        return toReturn

    def generateWhileLables(self) -> str:
        trueLabel = "While{0}True".format(self.whileCounter)
        falseLabel = "While{0}False".format(self.whileCounter)
        begin = "While{0}".format(self.whileCounter)
        self.whileCounter +=1
        return trueLabel, falseLabel, begin