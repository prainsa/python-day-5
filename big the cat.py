cp = int(input("Enter cost price"))
sp = int(input("Enter selling price"))
if (sp > cp):
    print("profit")
    p = sp - cp
    print("profit amount",p)
else:
    print("no profit only loss")
    
