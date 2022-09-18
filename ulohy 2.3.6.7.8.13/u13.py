print("Zadaj strany trojuholnika a,b,c:")
a = input("a:")
a = int(a)
b = input("b:")
b = int(b)
c = input("c:")
c = int(c)

if a+b > c and c+b > a and a+c > b:
    if a != b != c:
        if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
            print("Trojuholnik je pravouhly")
        else:
            print("Trojuholnik je roznostranny")
    elif a == b != c or c == b != a or a == c != b:
        print("Trojuholnik je rovnoramenny")
    elif a == b == c:
        print("Trojuholnik je rovnostranny")
else:
    print("Trojuholnik so stranami a,b,c neexistuje")
