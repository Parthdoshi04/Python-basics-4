x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
try:
    z=y/x
    print(z)
except Exception as e:
    print("Exception occured",e)
    z=None
else:
    print("No exception occured")
finally:
    print("The program is exceuted irrespective of exception")
print("Value of z is: ",z)
