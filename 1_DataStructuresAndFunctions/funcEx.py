def my_sum(*args):
    result = 0

    for x in args:
        result += x
    return result



def concatenate(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg+" "
    return result


#passing a args tuple as parameter
print(my_sum(1, 2, 3))

#passing dict **kwargs as parameter
print(concatenate(a="Hello", b="There", c="General", d="Kanobi", e="!"))
