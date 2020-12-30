class observable:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def update_observers(self, *args,**kwargs):
        for observer in self.observers:
            observer.update(*args,**kwargs)


class observer:

    pass

class AmericanStockMarket(observer):

    def update(self, *args, **kwargs):
        print("ASM Received : {0}\n{1}".format(args,kwargs))

class EuropeanStockMarket(observer):

    def update(self, *args, **kwargs):
        print("ESM Received : {0}\n{1}".format(args,kwargs))
