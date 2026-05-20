#first order objects -- functions
#normal function definition
def welcome_message():
    return 'Welcome to AI Batch May 2026'

res = welcome_message()           #function call
print(res)

#1. assigning function to a variable
var_fun = welcome_message          #assign welcome_message to var_fun
res_1 = var_fun()
print(res_1)
print(type(res_1))

def check_eligibility(age : int):
    if age >= 18:
        return True
    else:
        return False

var_res_2 = check_eligibility
print(type(var_res_2))
var_1 = var_res_2(5)
print(var_1)
print(type(var_1))
print(var_res_2(76))

#2. nesting functions - function inside function
def some_fun_1():
    def print_data(name : str):
        print(name)
    print_data("Pranita")

some_fun_1()

#3. passing function as an argument
def maths_operation(val1, val2,op):
    return op(val1, val2)

def add_1(n1, n2):
    return n1 + n2

def subtract_1(n1, n2):
    return n1 - n2

def multiply_1(n1, n2):
    return n1 * n2

var_add = maths_operation(10,10,add_1)
var_sub = maths_operation(13,78,subtract_1)
var_mul = maths_operation(10,5,multiply_1)
print(var_add)
print(var_sub)
print(var_mul)

#4. function as a return type
def get_operator(i : int):
    if i == 1:
        return add_1
    elif i == 2:
        return subtract_1
    elif i == 3 :
        return multiply_1
    else:
        return None

#get_operator() is returning functions and get_operator is passed as an argument to maths_operations function
res_a = maths_operation(5,25,get_operator(1))
print(res_a)