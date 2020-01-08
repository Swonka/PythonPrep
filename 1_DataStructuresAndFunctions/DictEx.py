input_list =[1,2,3,4,5,6,7]



def withFoorLoop():

    output_dict = {}
    
    for var in input_list:
        if var % 2 !=0:
            output_dict[var]=var**3

    print(output_dict)

def withComp():
    dict_using_comp = {var : var **3 for var in input_list if var %2 !=0}
    
    print(dict_using_comp)

withFoorLoop()
withComp()