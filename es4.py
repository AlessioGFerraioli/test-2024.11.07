'''
es4

crea un sistema che permetta di ordinare da varie classi figlie di autoffcine

ogni autofficina deve avere disponibile una funzoine per
riparare un tipo specifico di veiclo

richeide:classe autofficine (min 2 figli) 
classe veicolo (min 2 figli)
classe app_riparazioni (gestore)

'''

class Autofficina:
    def __init__(self, nome, specializzazione):
        self.__nome = nome
        self.__specializzazione = specializzazione

    def get_nome(self):
        return self.__nome
    
    def get_specializzazione(self):
        return self.__specializzazione

    def ripara_auto(self):
        print("Auto riparata")


class Motofficina(Autofficina):
    
    def ripara_moto(self, moto):
        print("Moto riparata")

class Camionficina(Autofficina):
    
    def ripara_camion(self, camion):
        print("camion riparata")



class Veicolo:
    def __init__(self, marca, modello):
        self.__marca = marca
        self.__modello = modello


class Auto(Veicolo):
    def __init__(self, marca, modello, n_porte):
        super().__init__(marca, modello)
        self.__n_porte = n_porte

    def get_n_porte(self):
        return self.__n_porte


class Moto(Veicolo):
    def __init__(self, marca, modello, sportivo):
        super().__init__(marca, modello)
        self.sportivo = sportivo

    def get_sportivo(self):
        return self.__sportivo


class App_Riparazioni:

    def __init__(self, lista_motofficine, lista_camionficine):
        self.lista_motofficine = lista_camionficine

    def ripara_veicolo(self, veicolo):
        if isinstance(veicolo, Moto):
            self.lista_motofficine[0].ripara_moto()
        elif isinstance(veicolo, Camion):
            self.lista_camionficine[0].ripara_camion()



