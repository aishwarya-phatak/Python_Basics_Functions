#lambda or anonymous functions
max_1 = lambda m,n : m if m > n else n
print(max_1(13,20))
print(max_1(45,1))

#normal way writing functions
def max_of_numbers(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

#filter function -- higher order function
def chk_positive(n):
    if n > 0:
        return True
    else:
        return False

list_1 = [34,-1,-3,0,97,66]
filtered_list = list(filter(chk_positive,list_1))
print(filtered_list)

#filter with lambda functions
filtered_list_2 = list(filter(lambda i : True if i > 0 else False,list_1))
print(filtered_list_2)