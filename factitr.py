n=int(raw_input("Enter the number:"))
k=n;
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of " + str(k)+": " + str(fact))
