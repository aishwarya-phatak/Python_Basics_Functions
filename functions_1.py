#functions

def welcome_message():
    print("\n Welcome To Bitcode!")
    print("\n This is AI May Batch!")

welcome_message()

#function definition
def check_even_odd(start_index : int, end_index: int):
    for i in range(start_index,end_index):
        if i % 2 == 0:
            print("{} is even".format(i))
        else:
            print("{} is odd".format(i))

check_even_odd(20,31)       #function call

def factorial_of_number(n : int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact

fact_res = factorial_of_number(5)
print(fact_res)


# def check_even_odd1(s_index,e_index):
#     for i in range(s_index,e_index):
#        assert i % 2 == 0 , "Number is odd"
#        print(i)
#
# check_even_odd1(4,21)

def check_even(num : int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

print(check_even(13))