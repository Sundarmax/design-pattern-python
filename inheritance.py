class Pet():

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __str__(self):
        return "%s is a %s " % (self.name,self.species)


class Dog(Pet):

    def __init__(self,name,chase_cats):
        '''Overloading example'''
        super().__init__(name,"Dog")
        self.chase_cats = chase_cats

    def __str__(self):
        additional_info = ""
        if self.chase_cats:
            additional_info = " Who chases cats"
        return super().__str__() + additional_info

class A(object):
    def __init__(self):
        print('A')

    @staticmethod
    def foo():
        print('foo')

class B(object):
    def __init__(self):
        print('B')

    @staticmethod
    def bar():
        print('bar')

# classes ordering 
class C(B,A):
    def foobar(self):
        self.foo()
        self.bar()


