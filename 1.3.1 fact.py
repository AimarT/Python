def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
     check = 5
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