s = "Hello world"

def print_hello(world):
    print(world)
    print(world)
    print(world)

def looping(number):
    for i in range(number):
        print(i)

if __name__ == '__main__':
    hello_world = "%s" % s
    a = 10
    print_hello("Hello")
    print("%s" % hello_world)
    print("%s" % "Hello python")
    print("Whats up")
    looping(5)
