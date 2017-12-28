def recfact(n):
   if n == 1:
       return n
   else:
       return n*recfact(n-1)
x=int(raw_input("enter the number\n"))
res=recfact(x)
print ("factorial of "+ str(x) +": "+ str(res))
