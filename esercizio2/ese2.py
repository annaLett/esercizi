import sys
import psutil

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



def stampa_menu() -> str:
    scelta_utente = input("""
Seleziona una statistica:

1. Versione Python
2. Percorso dell'eseguibile di Python
3. Spazio disco totale
4. Percentuale RAM usata
5. Numero di CPU logiche
6. Piattaforma sistema operativo

Inserisci la tua scelta (oppure X per uscire): 
"""
        )
    return scelta_utente
    
def menu_psutil() -> None:
    while True:
        scelta_utente = stampa_menu()

        # Esci dal programma
        if scelta_utente.upper() == "X":
            print("Uscita dal programma.")
            break

        # Controllo input numerico
        if not scelta_utente.isdigit():
            print("******************Inserire solo valori numerici (1-6)****************")
            continue

        scelta_utente = int(scelta_utente)

        if scelta_utente == 1:
            print("---------------->La versione di Python è:", sys.version)

        elif scelta_utente == 2:
            print("---------------->Il percorso dell'eseguibile di Python è:", sys.executable)

        elif scelta_utente == 3:
            print("---------------->Lo spazio disco totale è:", psutil.disk_usage('/').total)

        elif scelta_utente == 4:
            print("---------------->La percentuale RAM usata è:", psutil.virtual_memory().percent)

        elif scelta_utente == 5:
            print("---------------->Il numero di CPU logiche è:", psutil.cpu_count())

        elif scelta_utente == 6:
            print("---------------->La piattaforma del sistema operativo è:", sys.platform)

        else:
            print("******************Inserisci un numero compreso tra 1 e 6****************")
            
menu_psutil()
