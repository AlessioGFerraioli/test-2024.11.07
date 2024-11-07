'''
crea un sistema ripetibile che si occupi di 

dividere su tre possibili liste i tipi basilari di dato
che riceve in entrata. 
deve poter stampare una lista singola o tutte

richiede : un oggetto come esecutore.


'''


class CategorizzaDati:

    def __init__(self):
        self.__lista_num = []
        self.__lista_str = []
        self.__lista_bool = []
    
    def aggiungi_nuovo_dato(self, dato):
        if type(dato) == float or type(dato) == int:
            print(f"{dato}: Dato Numerico")
            self.get_lista_num().append(dato)
        elif type(dato) == str:
            print(f"{dato}: Dato Stringa")
            self.get_lista_str().append(dato)
        elif type(dato) == bool:
            print(f"{dato}: Dato Booleano")
            self.get_lista_bool().append(dato)

    def get_lista_num(self):
        return self.__lista_num
    
    def get_lista_str(self):
        return self.__lista_str
    
    def get_lista_bool(self):
        return self.__lista_bool
    
    def stampa_lista(self, nome):
        if nome == "num":
            print("Lista numerici")
            print(self.get_lista_num())
        elif nome == "str":
            print("Lista stringhe")
            print(self.get_lista_str())
        elif nome == "bool":
            print("Lista booleani")
            print(self.get_lista_bool())

    def stampa_tutte_le_liste(self):
        self.stampa_lista("num")
        self.stampa_lista("str")
        self.stampa_lista("bool")



# ESEMPIO DI UTILIZZO

# instanziazione
categorizzatore = CategorizzaDati()

# aggiungere dati
categorizzatore.aggiungi_nuovo_dato(3)
categorizzatore.aggiungi_nuovo_dato(3.3)
categorizzatore.aggiungi_nuovo_dato(True)
categorizzatore.aggiungi_nuovo_dato(False)
categorizzatore.aggiungi_nuovo_dato("ca")
categorizzatore.aggiungi_nuovo_dato("c")

# stampa lista numerica
categorizzatore.stampa_lista("num")

# stampa tutte le liste
categorizzatore.stampa_tutte_le_liste()