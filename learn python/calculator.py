a = int(input("Enter your first no.: "))
op = str(input("Enter your operator: "))
b = int(input("Enter your Second no."))

def add():
    if op == "+":
        c = (a+b)
        print(c)
        return c 
    else:
        print("um...")