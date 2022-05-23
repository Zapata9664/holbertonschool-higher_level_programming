#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        string = ""
        while count < x:
            string += str(my_list[count])
            count = count+1
            print(string)
    except:
        print(string)
    return(count)