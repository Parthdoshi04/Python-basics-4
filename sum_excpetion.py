try:
    sum=0
    n=int(input("Enter value till where you want sum: "))
    for x in range(1,n+1):
        sum=sum+x
    print("Sum is: ",sum)
except Exception:
    print("Enter value except 0 and alphabet")
