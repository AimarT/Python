def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    check = 5
    if int(number) < check:
        print("Sisesetatud number on väiksem, kui kontrollitav")
        loto()
    elif int(number) > check:
        print("Sisesetatud number on suurem, kui kontrollitav")
        loto()
    else:
        print("Palju õnne! Minge auhinnale järgi.")
loto()
        
     