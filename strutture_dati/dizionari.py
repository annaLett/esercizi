personaggio1:dict [str,str|int] = {      #nelle quadre ho [tipo chiave,tipo valore che posso indicare sempre con | per indicare che possono essere diversi]
    "nome":"pippo",
    "tipo":"cane",
    "email":"pippo@disney.com",
    "telefono": 3324567432
}

print(personaggio1)
print(personaggio1["email"])
print(personaggio1.get("telefono")) #utilizzo la funzione get()
print(personaggio1.get("eta")) #controllo se esiste eta, col get non da errore ma none
personaggio1["eta"] = 90 #creo chiave valore eta 90 
print(personaggio1.get("eta")) #90
#sprint(personaggio1) #è cambiata la struttura del dizionario

for chiave, valore in personaggio1.items():
    print(f"{chiave}:{valore}")