#This module is imported by to_run_module.py
#This module is responsible for taking inputs from the user.
#This module handles the exceptions during the input.
#Aashman Uprety, 26th May, 2020

def check_for_integer(number):
    """Definong a function to only alow the inputs to be in an integer form."""
    
    try:
        int(number)    
        return True
    except ValueError:
        return False
    
def user_input_module():
    """Defining a function to take inputs from the user."""

    fcheck = "no"
    scheck = "no"
    last_check = "no"
    

    while last_check == "no" :
        while fcheck == "no" :
            fniput = input("Enter first number: ")
            if check_for_integer(fniput) == False:    
                print("In order to add, the data type must be integer. So, please re-check and enter.")
            else:
                fnumber = int(fniput)
                if fnumber > -1 and fnumber < 256 :
                    fcheck = "yes"
                else:
                    print("As we are using 8 bit adder, please bear in mind that only numbers between 0-255 is acceptable. So, please re-check and enter.")
        while scheck == "no" :
            sinput = input("Enter second number: ")
            if check_for_integer(sinput) == False:
                print("In order to add, the data type must be integer. So, please re-check and enter.")
            else:
                snumber = int(sinput)
                if snumber > -1 and snumber < 256 :
                    scheck = "yes"
                else:
                    print("As we are using 8 bit adder, please bear in mind that only numbers between 0-255 is acceptable. So, please re-check and enter.")
        if (fnumber + snumber) > 255 :
            print("The sum of the two numbers inputted is greater than 255 which is not possible as we are using 8-bit adder. So, please re-check and enter")
            fcheck = "no"
            scheck = "no"

        else:
            last_check = "yes"
            return[fnumber,snumber]    # A list containing the inputted numbers is returned
