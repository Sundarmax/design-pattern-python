# SOURCE : https://www.djangospin.com/design-patterns-python/proxy/
# Proxy Design pattern. 
# 
class Car:
    '''Resource intensive object'''
    def driveCar(self):
        print("Driving Car... ")
 
class CarProxy:
    '''Relatively less resource-intensive proxy acting as middleman. Instantiates a Car object only if the driver is of age.'''
    def __init__(self):
        self.car = None
        self.age_of_driver = 15
    
    def driveCar(self):
        print("Proxy in action. Checking to see if the driver is of age or underage...")
        if self.age_of_driver >= 18:
            self.car = Car()
            self.car.driveCar()
        else:
            print("Driver is underage . Can't drive the car")
