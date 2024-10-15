a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
d=b**2-4*a*c
if d>0:
  root1=(-b+(d)**0.5)/(2*a)
  root2=(-b-(d)**.05)/(2*a)
  print("the roots are ",root1," and ",root2)
elif d==0:
  root=-b/(2*a)
  print("the root is ",root)
else:
  print("the eqn has no real roots")
