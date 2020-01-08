#functions are objects

def function1():
    print("called function1")

def function2(f):
    f()

def function3(func):
    def wrapper(*args, **kwargs):
        print("started")
        val = func(*args, **kwargs)
        print("Ended")
        return val


    return wrapper



@function3
def function0(sentence):
    print(sentence)

@function3
def add(x,y):
    return x+y

#function1()
#print(function1)
#function2(function1)

#function3(function1)()

#non decorator line
#f0 =function3(function0)
#f0()

function0("Hello")
print(add(4,5))