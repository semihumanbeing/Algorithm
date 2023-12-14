def hello(count):
    if count > 99:
        return 
    print("hi")
    hello(count + 1)

hello(0)