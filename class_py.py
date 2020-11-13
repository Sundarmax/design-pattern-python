# Understanding “__repr__” and “__str__” in Python
# Use python shell to verify the solution.
'''
__str__ or str() is used for creating output that is human-readable are must be for end-users. But, repr() or 
__repr__ must serve the purpose of debugging and development.

'''
class Animal:

    def __init__(self,animal,breed):
        self.animal = animal
        self.breed   = breed

    def __str__(self):
        #return "A {self.breed} {self.animal}".format(self=self)
        return "You just called __str__"
    
    def __repr__(self):
        return "You just called __repr__"

a = Animal("Dog","Pomeranian")
print(a)
print(a.animal)
print(a.breed)
