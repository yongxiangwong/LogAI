def decorator_test(func):
    def outer():
        print('This is outer function.')
        func()
    return outer()

@decorator_test
def inner():
    print('This is inner function.')

inner