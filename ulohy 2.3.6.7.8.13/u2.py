print("Zadaj interval <a,b>")
a = input("a:")
a = int(a)
b = input("b:")
b = int(b)

x = input("Zadaj cislo a zisti ci patri do intervalu:")
x = int(x)

interval = "<" + str(a) + "," + str(b) + ">"

if x >= a and x <= b:
    print("Cislo patri do intervalu", interval)
else:
    print("Cislo nepatri do intervalu", interval)
