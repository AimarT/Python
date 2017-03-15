from random import randint
check = randint(0,9)
#tõstsin funksioonist välja, et ei jääks korduma.

def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
     print(check)
     number =int(number)
     if number < check:
         print("Sisesetatud number on väiksem, kui kontrollitav")
         loto()
     elif number > check:
         print("Sisesetatud number on suurem, kui kontrollitav")
         loto()
     else:
         print("Palju õnne! Minge auhinnale järgi.")
    else:
         print("Numbrit taheti sa igavene tainas")
loto()