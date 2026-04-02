# Errori comuni in Python

## Errori su collezioni (liste, tuple, dizionari)

```python
#Errore index non trovato
IndexError: list index out of range 

#Errore di insert su una tupla, non si puo aggiungere poichè sono immutabili
TypeError: 'tuple' object does not support item assignment 

#Errore chiave non trovata, ad esempio in un dizionario
KeyError: 'key'
```

---

## Errori di tipo e conversione dati

```python
#Errore di conversione, non si può convertire una stringa in un numero intero
ValueError: invalid literal for int() with base 10: 'abc'

#Errore di attributo, la stringa non ha il metodo append, che è invece presente nelle liste
AttributeError: 'str' object has no attribute 'append'
```

---

## Errori matematici

```python
#Errore di divisione per zero, non si può dividere un numero per zero
ZeroDivisionError: division by zero

#Errore di overflow, un numero intero è troppo grande per essere convertito in un tipo di dato supportato
OverflowError: int too large to convert
```

---

## Errori su file e sistema

```python
#Errore di file non trovato, il file specificato non esiste
FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
```

---

## Errori di importazione moduli

```python
#Errore di importazione, il modulo specificato non esiste o non è installato
ImportError: No module named 'module'
```

---

## Errori di sintassi

```python
#Errore di sintassi, il codice non è scritto correttamente secondo le regole del linguaggio Python
SyntaxError: invalid syntax

#Errore di indentazione, il codice non è indentato correttamente, ad esempio con spazi o tabulazioni non coerenti
IndentationError: unexpected indent
```

---

## Errori di nome (variabili o funzioni)

```python
#Errore di nome, la variabile o funzione specificata non è definita nel contesto in cui viene utilizzata
NameError: name 'variable' is not defined
```

---

## Errori di esecuzione (runtime)

```python
#Errore di runtime, si verifica durante l'esecuzione del programma, ad esempio quando si verifica un'eccezione non gestita
RuntimeError: unhandled exception
```

---

## Errori di memoria

```python
#Errore di memoria, il programma ha esaurito la memoria disponibile
MemoryError: out of memory
```

---

## Errori di ricorsione

```python
#Errore di ricorsione, la profondità massima di ricorsione è stata superata, ad esempio quando una funzione chiama se stessa senza una condizione di terminazione adeguata
RecursionError: maximum recursion depth exceeded
```