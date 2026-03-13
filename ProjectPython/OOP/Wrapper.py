def decorator(func):
    def wrapper():
        print("Sebelum dieksekusi")
        func()
        func()
        print("sesudah dieksekusi")
        func()
    return wrapper

@decorator
def egiluy():
    print("yaitu")

egiluy();