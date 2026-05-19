#returning multiple values from a function

def calculate_sum_diff(num1 : int, num2 : int):
    sum_1= num1 + num2
    diff_1 = abs(num1 - num2)
    mul_1 = num1 * num2
    div_1 = num1 / num2
    return sum_1,diff_1,mul_1,div_1

res_sum, res_diff, res_mul,res_div = calculate_sum_diff(13,45)
print(res_sum, res_diff, res_mul, res_div)

#not returning a value only returning the control to function
#check negative
def check_negative(n):
    if n < 0:
        return
    else:
        print("{} is positive".format(n))

check_negative(10)