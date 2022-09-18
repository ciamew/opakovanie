cislo = input("Zadaj cislo:")
cislo = str(cislo)

predposledne =int(cislo[-2])
posledne = int(cislo[-1])

sucet = predposledne + posledne
print("Sucet:", sucet)
if sucet % 2 ==0:
    print("Sucet poslednych cifier je kladny")
else:
    print("Sucet poslednych cifier nie je kladny")