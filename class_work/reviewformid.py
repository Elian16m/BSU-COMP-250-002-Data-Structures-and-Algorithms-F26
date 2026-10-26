# my_list = ['x','y']

# my_list.append('z')
# my_list.insert(0,'o')
# my_list.remove('y')
# pop = my_list.pop()
# print(pop)
# print(my_list)

def fact(n):
    if n <= 1:          # BASE CASE: stop here
        return 1
    return n * fact(n-1)  # RECURSIVE CASE: calls itself with a smaller n
a = fact(5)
print(a)