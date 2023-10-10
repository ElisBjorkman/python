import random

#skapar frukter
frukter = ("Apel", "Carrot", "Päron")

def print_fruit (userinput):
    fnr = int(userinput)
    print(f"\n {frukter[fnr-1]} kommer här! \n")

while True:

    print ("--------------------------------------")
    print (f"\n FruktAutomat \n")

    i = 1
    for frukt in frukter:
        print (f"{str(i)} : {frukt}")
        i += 1


    fruktnr = input ("\nMata in siffra för vald frukt: ")


    print_fruit (fruktnr)
    

    go = input("Vill du välja en frukt till? j/n ")
    print ("\n")

    if (go == "n"):
        break

print ("----------------------------------------")
print ("Föresten, du får en frukt till!")
slumpfruktnr = random.randint(1, 3)
print_fruit(slumpfruktnr)