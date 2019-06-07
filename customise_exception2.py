class invalid(Exception):
    def __init__(self,z):
        super().__init__(z)
class demo:
    def get(self,x):
        if '*' in x:
            print("All Is Well")
        else:
            raise invalid("* is mandatory")
try:
        d1=demo()
        d1.get("Hello")
except invalid as c:
        print(c)
