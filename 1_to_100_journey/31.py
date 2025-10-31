#write a function to check prime.
num = int(input("enter a no. :"))
b=0
for a in range(1,num+1):
    if num % a == 0: b += 1

if b == 2: print(f'prime no. :{b}')
else: print(f'not prime no. :{b}')



#pythonic
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not prime number")

#shorter pythonic
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not prime")

