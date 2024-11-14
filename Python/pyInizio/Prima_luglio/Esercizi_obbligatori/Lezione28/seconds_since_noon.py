"""Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi."""

def seconds_since_noon(hours: int, minutes: int, seconds: int) -> int:
    # Calcola il numero di secondi passati dalle 12:00:00
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

def time_difference(hours1: int, minutes1: int, seconds1: int, hours2: int, minutes2: int, seconds2: int) -> int:
    # Calcola i secondi passati dalle 12:00:00 per entrambi gli orari
    seconds1 = seconds_since_noon(hours1, minutes1, seconds1)
    seconds2 = seconds_since_noon(hours2, minutes2, seconds2)
    
    # Calcola la differenza in secondi tra i due orari
    difference = abs(seconds2 - seconds1)
    return difference
