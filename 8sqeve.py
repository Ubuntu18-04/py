def is_square(n):
    if int(n**0.5)==n**0.5:
        return True
    else:
        return False
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input("Enter upperlimit:"))
for i in range(2,n+1):
    if is_even(i) and is_square(i):
        print(i)