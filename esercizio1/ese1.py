'''
Obiettivo
Creare un semplice quiz che
1 pone una domanda a scelta multipla
2 raccoglie la risposta dell'utente
3 fornisce un feedback.

Requisiti

1. Setup della domanda
Definire una domanda (es: "Qual è il tuo linguaggio di programmazione preferito?")
Definire 4 opzioni di risposta (es: 1-Python, 2-JavaScript, 3-Java, 4-C++)

2. Raccolta risposta
Mostrare la domanda e le 4 opzioni
Chiedere all'utente di inserire un numero da 1 a 4 usando input()
Convertire la risposta in int

3. Elaborazione e feedback
Usare if/elif/else per identificare quale opzione è stata scelta
Mostrare un messaggio personalizzato per ogni scelta
Esempi di messaggio:
"Ottima scelta! Perché lo useremo per i prossimi quattro mesi!"
"Interessante! Ma mi vuoi male!"
"Solida scelta! Ok, però si potrebbe fare meglio! Tipo Python!"
"Potente! C++ è ottimo per le performance, ma lasciamolo ai nerd!"

4. Gestione errori
Se l'utente inserisce un numero non valido (non 1-4), mostrare un messaggio di errore
Esempio: "Errore: devi scegliere un numero tra 1 e 4"
Suggerimenti
Puoi personalizzare domanda e opzioni come preferisci
Testa il programma con input diversi (1, 2, 3, 4 e anche numeri non validi come 5 o 0)
'''
programma_preferito = int(input("Qual è il tuo linguaggio di programmazione preferito?\n\n1. Python \n2. JavaScript \n3. Java \n4. C++\n\nInserire un numero da 1 a 4\n"))
if programma_preferito == 1:
	print(f"Hai scelto {programma_preferito}. \nOttima scelta! Perché lo useremo per i prossimi quattro mesi!")
elif programma_preferito == 2:
	print(f"Hai scelto {programma_preferito}. \nInteressante! Ma mi vuoi male!")
elif programma_preferito == 3:
	print(f"Hai scelto {programma_preferito}. \nSolida scelta! Ok, però si potrebbe fare meglio! Tipo Python!")
elif programma_preferito == 4:
	 print(f"Hai scelto {programma_preferito}. \nPotente! C++ è ottimo per le performance, ma lasciamolo ai nerd!")
else:
   print("Errore: devi scegliere un numero tra 1 e 4!")
