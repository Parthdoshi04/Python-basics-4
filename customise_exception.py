class invalid(Exception):
    pass
class demo:
    def get(self,x):
        if '*' in x:
            print("All Is Well")
        else:
            raise invalid
try:
        d1=demo()
        d1.get("Hello*")
except invalid:
        print("* not present")
