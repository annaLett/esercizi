stringhe: list [str] = ["pippo","pluto"]
stringhe.append("minnie") #aggiungo elemento alla lista


print(len(stringhe)) #stampo la lunghezza della lista --> 3
print(len(stringhe[1])) #stampo la lunghezza dell'elemento della lista --->5
print(stringhe) #['pippo', 'pluto', 'minnie']

for ele in stringhe: #stampo ogni elemento col ciclo for
    print(ele)
'''
stampa:
pippo
pluto
minnie
'''
#print("ho eliminato : " + stringhe.pop() + "\nora la lista è: ")#sto togliendo l'ultimo elemento
#print(stringhe)

deleted_values: list[str] = [] #inizzializzo la lsita vuota di valori eliminati

deleted_value = stringhe.pop() #deleted_value è uguale all'ultimo valore eliminato col pop()
deleted_values.append(deleted_value) #aggiungo con append il valore eliminato alla lista dei valori eliminati

print(stringhe) #['pippo', 'pluto']
print(deleted_values) #['minnie']

#deleted_value = stringhe.pop(1) #elimino l'elemento all'indice 1 e lo associo a deleted_value
#deleted_values.append(deleted_value) #aggiungo con append il valore eliminato alla lista dei valori eliminati

#print(stringhe) #['pippo']
#print(deleted_values) #['minnie', 'pluto']

index_value_to_delete = stringhe.index("pluto") #index scorre la lista e trova pluto e ci dice l'indice
print(index_value_to_delete) #-->1
deleted_value = stringhe.pop(1) #elimino pluto in posizione 1
print(stringhe) #['pippo']


stringhe.append("pluto") #riaggiungo pluto
print(stringhe)
value_to_check_and_delete:str = "pluto" #inizzializzo la variabile così da poterla cambiare nel for all'occorrenza
is_the_value_in_the_list:bool = value_to_check_and_delete in stringhe #esempio con in

if is_the_value_in_the_list  == True:
    index_value_to_delete = stringhe.index(value_to_check_and_delete) #gli diamo pluto tramite variabile
    deleted_value = stringhe.pop(index_value_to_delete) #eliminiamo pluto con l'indice trovato
    deleted_values.append(deleted_value) #aggiungo pluto alla lista dei valori eliminati
    
    
print(stringhe)
print(deleted_values)


stringhe2 : list[int|str|list] = [] #indico che questa lista ha tipi misti tra cui liste