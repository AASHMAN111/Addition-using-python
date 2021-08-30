#This module takes two input from the user. The input can be numbers between 0 and 255.
#This module keeps on executing until the user wishes.
#This module can also be called as a main module.
#addition_module.py is imported in this module for the addition
#conversion_module.py is imported in this module for the conversion
#user_input_moduoe.py is imported in this module for taking the inputs from them and to handle exceptions.
#Aashman Uprety, 26th May, 2020

import addition_module
import conversion_module
import user_input_module

def list_to_string(lst):
    """Function to convert the list 'lst' to string."""
    
    string = ""
    for i in lst:
        i = str(i)
        string = string + i
    return string 

check = "yes"

while check != "no":
    if check == "yes":
        lst = user_input_module.user_input_module()
        
        fbinary = conversion_module.decimal_to_binary(lst[0])
        
        sbinary = conversion_module.decimal_to_binary(lst[1])
       
        bit_addition = addition_module.bit_addition(fbinary, sbinary)

        bitwise_add = addition_module.bitwise_addition(lst[0],lst[1])

        print("First inputted number in binary is: ", list_to_string(fbinary))
        print("Second inputted number in binary is: ", list_to_string(sbinary))
        print("Sum of the two inputted numbers in binary is: ", list_to_string(bit_addition))
        print("Sum of the two inputted numbers in decimal is: ",bitwise_add)

    else:
        print("please only enter yes or no.")
    check = input("Are you willing for another addition? If yes just type yes than you can else just type no, the program will terminate : ")
    check = check.lower()
    
if check == "no":
    print("The program is terminating. BYYEEEEEEEE.")
