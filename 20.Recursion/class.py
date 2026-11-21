def outer():
    def inner():
        print(list("This"))
        print(list)
    inner() 
outer()
