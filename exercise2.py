class invalid(Exception):
    pass
class user:
    def eid(self,emailid):
        if('@' and '.com') in emailid:
            print("Email id is correct")
        else:
            raise invalid
    def number(self,num):
        if((len(num)==10)) in num:
            print("Number is proper")
        else:
            raise invalid
    def empage(self,age):
        if(age<100) in age:
            print("Age is valid")
        else:
            raise invalid
try:
    emailid=input("Enter email id: ")
    num=int(input("Enter mobile number: "))
    age=int(input("Enter age of user: "))
    u=user()
    u.eid(emailid)
    u.number(num)
    u.empage(age)
except invalid:
    print("not prpoer")
