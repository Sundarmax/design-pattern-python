# Iterables and iterators. 

def test_iterators():
    numbers = [1,2,3,4,5]
    numbers = iter(numbers)
    print(next(numbers))

test_iterators()
