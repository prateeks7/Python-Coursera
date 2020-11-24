a=input("Enter a number: ")
n=int(a)
c=n
A=0
while c>0:
    d=int(c%10)
    A=(d**3)+A
    c=int(c/10)
if A == n:
   print ("Armstrong Number")
else:
   print("Not An Armstrong Number")
