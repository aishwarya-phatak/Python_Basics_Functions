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