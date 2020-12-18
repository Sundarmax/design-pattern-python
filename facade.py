# SOURCE : https://www.djangospin.com/design-patterns-python/facade/
# Facade design pattern. 
class ProcessingUnit:
    '''Subsystem #1'''
    def process(self):
        print("Processing..")


class DisplayUnit:
    '''Subsystem #2'''

    def display(self):
        print("Displaying..")

class MemoryUnit:
    '''Subsystem #3'''

    def iooperation(self):
        print("Reading and writing to memory..")

class Computer:
    ''' FACADE '''
    
    def __init__(self):
        self.processingUnit = ProcessingUnit()
        self.displayUnit = DisplayUnit()
        self.memoryUnit  = MemoryUnit()

    def bootUp(self):
        self.processingUnit.process()
        self.memoryUnit.iooperation()
        self.displayUnit.display()
