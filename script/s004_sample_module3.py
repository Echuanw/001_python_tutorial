def foo():
    pass

def bar():
    pass

# Only the name of the module that is directly executed by the Python interpreter is `__main__`
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()