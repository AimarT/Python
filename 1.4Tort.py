pikkus = input("Sisesta pikkus tükkides: ")
laius = input("Sisesta laius tükkides: ")
kõrgus = input("Sisesta kürgus tükkides: ")
tk_pakk = input("Mitu tükki on ühes pakis: ")

def pakke():
 tk_arv = int(pikkus)*int(laius)*int(kõrgus)
 pakk_arv = tk_arv/int(tk_pakk)
 print("Sul on vaja " + str(round(pakk_arv+0.49))+ " pakki")

pakke()

