

message='outer function'
def outer():
    def inner():
        print(message)
    inner()
    
outer()
