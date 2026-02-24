'''
Creare un array NumPy per estrarre e modificare sottoarray specifici utilizzando slicing.
    1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
    2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
    3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
    4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
    5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
    6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
    7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
'''

import numpy as np

arrei_int = np.random.randint(10, 51, 20)   # np.random.randint crea un array 1D di 20 numeri interi casuali tra 10 e 50

print("Array originale:", arrei_int)

arrei_int_primi_10 = arrei_int[:10]         # [:x] estrae i primi x elementi
arrei_int_ultimi_5 = arrei_int[-5:]         # [y:] estrae gli utlimi y elementi
arrei_int_tra_5_e_15 = arrei_int[5:15]      # [a:b] estrae gli elementi dall'indice a all'indice b (escluso)
arrei_int_ogni_3rd = arrei_int[::3]         # [::k] estrae ogni terzo elemento
arrei_int[5:10] = 99                        # [i:j] = c modifica gli elementi dall'indice i all'indice j (escluso) ponendoli uguali a c

print("Primi 10 elementi:", arrei_int_primi_10)
print("Ultimi 5 elementi:", arrei_int_ultimi_5)
print("Elementi dall'indice 5 al 15 (escluso):", arrei_int_tra_5_e_15)
print("Ogni terzo elemento:", arrei_int_ogni_3rd)
print("Array modificato:", arrei_int)