'''
Obiettivo
Creare un'applicazione a riga di comando che permette all'utente di visualizzare diverse statistiche di sistema usando le librerie sys e psutil.
Requisiti
1. Import e setup
```python
import sys
import psutil
```
2. Menu principale
Mostrare un menu numerato con almeno 6 opzioni di statistiche disponibili, ad esempio:
  1. Versione Python
  2. Piattaforma sistema operativo
  3. Memoria RAM totale (in bytes)
  4. Memoria RAM disponibile (in bytes)
  5. Percentuale utilizzo CPU
  6. Numero di CPU logiche
  7. [Aggiungi altre che preferisci da sys o psutil]
3. Logica di selezione
- Chiedere all'utente quale statistica vuole visualizzare
- Usare `input()` per raccogliere la scelta
- Convertire l'input in intero usando `int()`
- Usare `if/elif/else` per chiamare la funzione appropriata di `sys` o `psutil`
- Mostrare il risultato esattamente come viene restituito dalla libreria
4. Formato output
Per ogni statistica, mostrare:
  - Un titolo descrittivo
  - Il valore restituito dalla libreria (senza conversioni)
5. Gestione opzione non valida
- Se l'utente inserisce un numero non presente nel menu, mostrare un messaggio di errore
- Esempio: "Opzione non valida. Scegli un numero tra 1 e 6."
'''

import sys
import psutil

scelta_utente = int(print("Seleziona una statistica:\n\n1. Versione Python\n2. Sistema Operativo\n3. RAM Totale\n4. RAM Disponibile\n5. Utilizzo CPU\n6. Numero CPU\n\nInserisci la tua scelta:"))
