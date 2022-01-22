def prime_checker(*number):
    for n in number:
        for i in range(2,n//2):
            if n % i == 0:
                print(f"{n} not prime")
                break        
        else:
            print(f"{n} PRIME")


# y = ([x for x in range(2,101)])
# print(y)

'''
print(*y)
This will print the list separated by spaces.
(where * is the unpacking operator that turns a list into positional arguments, print(*[1,2,3]) is the same as print(1,2,3)

'''

prime_checker(12,27,34,42,99,97)
