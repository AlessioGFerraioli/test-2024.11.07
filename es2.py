'''
es2

crea un sistema ripetibile che dopo aver preso in input X parole e/o numeri
e li aggiunge a una collezione,
si deve ripetere tante volte quante l'utente richiede
e poi stampare tutti gli elementi nella lista
che non si ripetono

richiede che ogni valore o aggregazione dell'oggetto siano incapsulati
'''




class ContenitoreDati:

    def __init__(self):
        self.__lista = []

    def get_lista(self):
        return self.__lista
    
    def __aggiungi_a_lista(self, dato):
        self.get_lista().append(dato)

    def __stampa_lista_senza_ripetizioni(self):
        print(list(set(self.get_lista())))

    def start(self):
        print("Contenitore di dati.")
        numero_dati = int(input("Quanti dati vuoi aggiungere? "))
        print(f"Aggiungiamo {numero_dati} dati.")
        for i in range(numero_dati):
            dato = input(f"Inserisci dato {i+1}: ")
            self.__aggiungi_a_lista(dato)
        print("\nDati inseriti correttamente.")
        print("Lista di dati inseriti (senza ripetizioni):")
        self.__stampa_lista_senza_ripetizioni()
        

# esempio di utilizzo
box = ContenitoreDati()
box.start()