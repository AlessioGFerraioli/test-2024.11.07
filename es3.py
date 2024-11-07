'''
es3

crea un sistema che permetta di valorizzare una lista di 5 numeri per due votle,
dopodiché somma ogni posizoine con la corrispettiva dell'altra aggregazione
e stampa i risultati.
alla fine chiedi se si vuole ripetere

richeide: l'uso di due oggetti, ognuno deve contenere una delle due
aggregazioni da confrontare.
il confronto deve avvenire in una funzione polimorfica

'''

class Registro:
    def __init__(self):
        self.__lista = []

    def get_lista(self):
        return self.__lista

    def inserisci_valutazione(self, valutazione):
        self.get_lista().append(valutazione)
    

class Teorico(Registro):
    def start(self):
        print("Inserimento valutazioni teoriche")
        print("Hai da inserire 5 valtuazioni teoriche.")
        
        for i in range(5):
            valutazione = float(input(f"Inserisci valutazione {i+1}: "))
            super().inserisci_valutazione(valutazione)
        print("Valutazioni teoriche inserite correttamente.")

class Pratico(Registro):
    def start(self):
        print("Inserimento valutazioni pratiche")
        print("Hai da inserire 5 valtuazioni pratiche.")
        
        for i in range(5):
            valutazione = float(input(f"Inserisci valutazione {i+1}: "))
            super().inserisci_valutazione(valutazione)
        print("Valutazioni pratiche inserite correttamente.")


def estrai_voti_da_registro(registro, posizione):
    return registro.get_lista()[posizione]

def somma_registri_voti(registro1, registro2):
    lista_somma = []
    if len(registro1.get_lista()) != len(registro2.get_lista()):
        print("I due registri hanno liste voti incompatibili. ")
    else: 
        numero_voti = len(registro1.get_lista())
    
        for i in range(numero_voti):
            somma = estrai_voti_da_registro(registro1,i) + estrai_voti_da_registro(registro2,i)
            lista_somma.append(somma)
    return lista_somma

registro_voti_teorico = Teorico()
registro_voti_pratico = Pratico()

continuare = True
while continuare == True:
    registro_voti_teorico.start()
    registro_voti_pratico.start()


    lista_somma = somma_registri_voti(registro_voti_teorico, registro_voti_pratico)
    print("Stampa lista voti combinata: ")
    print(lista_somma)

    print("\nVuoi aggiungere nuovi voti?")
    risposta = input("y/n: ")
    if risposta != "y":
        continuare = False

        