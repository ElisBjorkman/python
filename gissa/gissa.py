import random 

print("\n----------------------------")
print(".:GissaTalet:.")

print("Gissa ett tal mellan 1-10, du får 33 st försök!\n")
slumptal = random.randint(1, 10)
print(slumptal)
i=0
hittat = False



while i<3:
    gissatal = input("mata in ett tal")

    if slumptal == int(gissatal):
        hittat =True
        print("Grattis du får en fet smäll!")
        break

    i += 1 

    if hittat: 
        print("Du får en smäll till!")

    else:
        print("Bättre lycka nästa gång")

    print("___________________________________")
