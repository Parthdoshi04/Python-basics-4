try:
    mylist=[1,2,3,4,5]
    sum=0
    for i in mylist:
        sum=sum+i
    print(sum)
    print(mylist[5])
except ValueError:
    print("Vlaue Error")
except IndexError:
    print("Index Error")
