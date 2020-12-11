print("Calculator")
a = floa(input("enter ur First no. :"))
opr = str(input("enter ur operator :"))
b = float(input("enter ur second no. :"))

if opr == "+":
    print("sum of two no. is :",a+b)

elif  opr == "-":
    print("the diff between two no. is :",a - b)

elif opr == "*" or "x":
    print("the multiplication between two no. is :",a*b)

elif  opr == "/":
    print("the division between two no. is :",a/b)

else:
    print("unrecognised commands")
    
