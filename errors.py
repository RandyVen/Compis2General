class semanticError:
    def __init__(self, line, message):
        self.line = line
        self.message = message
    
    def __str__(self):
        return 'Error on line {0}:\n    {1}'.format(self.line, self.message)