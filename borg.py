# Singleton Borg pattern
class Borg:
    __shared_state  = {}
    
    # constructor method
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'GeeksforGeeks'

    def __str__(self):
        return self.state


# >>> b = Borg()
# >>> b.state
# 'GeeksforGeeks'
# >>> a.state
# 'GeeksforGeeks'
# >>> a.__dict__
# {'state': 'GeeksforGeeks'}
# >>> a.state = 'GGK'
# >>> b.state
# 'GGK'
# >>> a.state
# 'GGK'
# >>>


