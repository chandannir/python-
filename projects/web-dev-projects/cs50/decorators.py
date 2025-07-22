def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done runnning the function")
    return wrapper

@announce
def hello():
    print("hello World")
    
hello()

