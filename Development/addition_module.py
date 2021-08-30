#This module is imported by to_run_module.py module.
#This module consists of a function that behaves as a byte adder, and generates
#eight-bit sum of two binary values supplied from to_run_module.py
#Aashman Uprety, 26th May, 2020

def full_adder(carry_in, d, e):  #carry_in, d and e are the three inputs to pass in the module
    """."""
    
    added = (d ^ e) ^ carry_in
    carry_out = (carry_in & d) | (carry_in & e) | (d & e)
    return [carry_out,added] 

def bit_addition(d, e):
    """Defining a function that takes two lists as input and executes its sum and returns the sum in the form of a list."""
    
    add_list = [0,0,0,0,0,0,0,0] # defining a list that stores added binary number  
    carry = 0
    for i in range (7 , -1 ,-1):
        add_list[i] = full_adder(carry, d[i], e[i])[1]
        carry = full_adder(carry, d[i], e[i])[0]
    return(add_list) #returns a list
  
def bitwise_addition(d, e):
    """Defining a function for bitwise addition of number."""
    
    carry = d & e   
    added = d ^ e
    while carry > 0:
        shift_left = carry << 1
        carry = added & (carry << 1)
        added = added ^ shift_left   
    return added  #Integer value is returned.
    return added  #Integer value is returned.
