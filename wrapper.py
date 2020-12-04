import time

def time_function(my_function):
    def wrapper():
        t1 = time.time()
        my_function()
        t2 = time.time()
        print("Time It took to run the func :",str(t2-t1))
    return wrapper

@time_function
def my_function():
    output = []
    for num in (range(0,1000000)):
        output.append(num)
    print(len(output))
    #print("Sum of list",sum(output))

my_function()
