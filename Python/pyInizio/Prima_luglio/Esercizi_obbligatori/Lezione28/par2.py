"""Scrivere un frammento di codice che modifichi il valore intero memorizzato nella variabile n nel seguente modo:
se n è pari, deve essere incrementato di 10;
se n è dispari, deve essere decrementato di 5."""
def modifica_valore(n: int) -> int:
    if n &2==0:
        return n + 10
    else:
        return n - 5