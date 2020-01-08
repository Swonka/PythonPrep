input_list = [1,2,3,4,4,5,6,6,6,7,7]


def withFoorLoop():

    output_set = set()

    for var in input_list:
        if var % 2 == 0:
            output_set.add(var)
    print(output_set)

def withComp():
    set_using_comp = {var for var in input_list if var %2 == 0}
    print(set_using_comp)


withFoorLoop()
withComp()