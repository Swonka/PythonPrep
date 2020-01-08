def my_generator():
    n = 1
    print('This is printed first')
    
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

for item in my_generator():
    print(item)