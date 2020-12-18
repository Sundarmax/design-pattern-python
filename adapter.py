# Example #1: Square-pin to round-pin adapter
# Consider two incompatible interfaces: round-pin Socket & square-pin Electric Kettle.
# The Electric Kettle expects a square-pin connection for it to work.
# The Adapter takes square-pin of Electric Kettle, and connects to round-pin socket.

# The Adaptee
class Socket:
    _pinType = "Round"

# The Adapter
class Adapter:
    _socket = None
    _pinType = "SquareToRound"

    def __init__(self,socket):
        self._socket = socket

# The client 
class ElectricKettle:    
    _adapter  = None
    _pinType  = "Square"

    def __init__(self, adapter):
        self._adapter = adapter

    def makeTea(self):
        if self._adapter._pinType == (self._pinType + "To"+ self._adapter._socket._pinType):
            print("Cooking Maggi")
        else:
            print("No Power. Can't function")
