# def suma(n):
#     if n==1:
#         return 1
#
#     return n+suma(n-1)

# print (suma(10))

# S=0
# n=10
# for i in range(1,n+1):
#     S+=i
# print(S)


# def fib(n):
#     if n == 1    or n == 0:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(5))
#
def reverse_list(arr):
    if len(arr) == 1:
        return arr
    else:
        return[arr[-1]] + reverse_list(arr[:-1])
print (reverse_list([5,6,8,7,3]))



