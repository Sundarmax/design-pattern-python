class Singleton:

    __ins = None

    def __new__(cls,val=None):
        if Singleton.__ins is None:
            # Create new object if not exists
            Singleton.__ins = object.__new__(cls)
        Singleton.__ins.val = val
        return Singleton.__ins

# Test 
a = Singleton(4)
print(a.val)
b = Singleton(5)
print(b.val)
print(a.val)
# Singleton creates only one global object 
# Check the id below is same for two objects.  
print(id(a),id(b))