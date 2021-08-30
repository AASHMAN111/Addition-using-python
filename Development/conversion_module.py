#This module is imported by the main module to_run_module.py
#This module converts integer to 8-bit binary.
#Aashman Uprety, 26th May 2020

def decimal_to_binary(number):
    """Defining a function for the conversion of integer to 8-bit binary."""
    
    a = number
    b = [0,0,0,0,0,0,0,0]  # making a list to store 8-bit binary having length '8'.
    while a > 0:
        if a > 127:
            b[0] = 1
            a = a - 128
        elif a > 63 and a < 128:
            b[1] = 1
            a = a - 64
        elif a > 31 and a < 64:
            b[2] = 1
            a = a - 32
        elif a > 15 and a < 32:
            b[3] = 1
            a = a - 16
        elif a > 7 and a < 16:
            b[4] = 1
            a = a - 8
        elif a > 3 and a < 8:
            b[5] = 1
            a = a - 4
        elif a > 1 and a < 4:
            b[6] = 1
            a = a - 2
        elif a == 1:
            b[7] = 1
            a = 0
    return b        # A list is returned
