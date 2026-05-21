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

#formal vs actual parameters on string, int, float, tuple -- immutable objects
def check_even(num : int) -> bool:
    if num % 2 == 0:
        num += 2
        print(id(num))
        return True
    else:
        return False

number_one = 14
print(id(number_one))
print(check_even(number_one))

#formal vs actual parameters -- mutable objects -- list, dictionary
def change_case(l1 : list):
    for each_item in l1:
        print(id(l1))
        print(each_item.upper())

list_1 = ["Pooja","Pranita","dhanashri","vishal","roshni"]
print(id(list_1))
change_case(list_1)
print(list_1)

def change_case_1(l1 : list):
    for i in range(0,len(l1)):
        l1[i] = l1[i].upper()
        print(id(l1))

list_2 = ["Pooja","Pranita","dhanashri","vishal","roshni"]
print(id(list_2))
change_case_1(list_2)
print(id(list_2))
print(list_2)

list_2.append("Rutuja")
print(list_2)