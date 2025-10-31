#34. Recursive Fibonacci function.
def fibo_(a, b, n):
    if n == 0:
        return
    print(a, end=" ")
    fibo_(b, a + b, n - 1)

usr_inp = int(input("Enter how many terms: "))
fibo_(0, 1, usr_inp)

