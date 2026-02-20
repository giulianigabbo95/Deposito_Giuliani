dizionario = {
    "antonio": ["1", "2", "3"],
    "giuseppe": ["4", "5", "6"]
}

stringa = "emanuela,9-8-7\nbeatrice,6-5-4"

def convertiDict(dizionario):
    strg = ""                                   #Stringa
    for chiave, valore in dizionario.items():
        # val = "-".join(valore) # val = "-".join(map(str, valore))
        # strg += f"{chiave},{val}\n"
        strg += f"{chiave},{"-".join(valore)}\n" # "-".join(valore) = "-".join(map(str, valore))
    print(strg.strip("\n"))
    return strg.strip("\n")

def convertiStr(stringa):
    diz = {}
    lista_strg = stringa.split("\n")            #Stringa
    for riga in lista_strg:
        parti = riga.split(",")                     #Stringa
        chiave = parti[0]                           #Stringa
        valore = parti[1]                           #Stringa
        elementi = valore.split("-")                #Lista di Stringhe Numeriche
        numeri = list(map(int, elementi))           #Lista di Interi
        diz[chiave] = numeri
    print(diz)
    return diz



print("")
print("da Dizionario a Stringa:")
diz_to_str = convertiDict(dizionario)
print("")
print("da Stringa a Dizionario:")
str_to_diz = convertiStr(stringa)
print("")
