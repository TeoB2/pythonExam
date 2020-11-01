#import constants
import statistics
from itertools import cycle

#dizionario contentente tutte le materie
materie = {
            1: 'Informatica', 
            2: 'Economia', 
            3: 'Diritto', 
            4: 'Sociologia'
        }

#dizionario con le azioni che si possono effettuare
azioni = {
            1: 'Inserisci voto',
            2: 'Vedi voti'
        }

#liste contenti i voti delle materie
votiInformatica = []
votiEconomia = []
votiDiritto = []
votiSociologia = []


def inizializzaScript():

    #inizializzo gli errori a false
    error = False

    #ciclo le materie disponibili
    for key,value in list(materie.items()):
        print("{}) {}".format(key,value))

    materiaSelezionata = input("Seleziona la materia:\n")

    #controllo se l'azione selezionata è un intero
    try:
        #sanitizzo l'intero
        materiaSelezionata = int(materiaSelezionata)

        if (type(materiaSelezionata) != int):
            #setto gli errori
            error = True

    except:
            #setto gli errori
            error = True
    
    #controllo se la materia selezionata esiste e se è un intero
    if (not error and materiaSelezionata >= 1 and materiaSelezionata <= 4):
        #ciclo le materie disponibili
        for key,value in list(azioni.items()):
            print("{}) {}".format(key,value))

        azioneSelezionata = input("Vuoi inserire un voto o vederli?\n")

        #controllo se l'azione selezionata è un intero
        try:
            #sanitizzo l'intero
            azioneSelezionata = int(azioneSelezionata)

            if (type(azioneSelezionata) != int):
                #setto gli errori
                error = True

        except:
            #setto gli errori
            error = True

        if (not error and azioneSelezionata == 1):
            inserisciVoto(materiaSelezionata)
                   
        elif (not error and azioneSelezionata == 2):
            vediVoti(materiaSelezionata)

        else:
            print("L'azione che hai selezionato non esiste\n")

    else:
        print("Seleziona una materia esistente\n")


#permette l'inserimento di un voto di una determinata materia
def inserisciVoto(materiaSelezionata):
    votoInserito = input('\nInserisci il voto della materia ' + materie[materiaSelezionata].lower() + ':\n')

    #controllo se il voto selezionato è un intero
    votoInserito = int(votoInserito)

    if (votoInserito > 17 and votoInserito <= 30):
        if (materiaSelezionata == 1):
            votiInformatica.append(votoInserito) 

            print('È stato inserito il voto ' + str(votoInserito) + ' alla materia ' + materie[materiaSelezionata].lower() + '\n')

        elif (materiaSelezionata == 2):
            votiEconomia.append(votoInserito) 

            print('È stato inserito il voto ' + str(votoInserito) + ' alla materia ' + materie[materiaSelezionata].lower() + '\n')

        elif (materiaSelezionata == 3):
            votiDiritto.append(votoInserito)

            print('È stato inserito il voto ' + str(votoInserito) + ' alla materia ' + materie[materiaSelezionata].lower() + '\n') 

        elif (materiaSelezionata == 4):
            votiSociologia.append(votoInserito)

            print('È stato inserito il voto ' + str(votoInserito) + ' alla materia ' + materie[materiaSelezionata].lower() + '\n')

        else:
            print('C\'è stato un problema con il sistema, riprovare per piacere\n')

    else:
        print('Il voto inserito deve essere compreso tra 1 e 30!\n')


#visualizza i voti e la media della materia selezionata
def vediVoti(materiaSelezionata):

    if (materiaSelezionata == 1):
        #controllo se ci sono voti inseriti
        if not votiInformatica:
            print('La materia ' + materie[materiaSelezionata].lower() + ' non ha voti inseriti\n')

        else:
            print('\n')
            for voto in range(len(votiInformatica)): 
                print(votiInformatica[voto]), 

            print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiInformatica))) + '\n')

    elif (materiaSelezionata == 2):
        #controllo se ci sono voti inseriti
        if not votiEconomia:
            print('La materia ' + materie[materiaSelezionata].lower() + ' non ha voti inseriti\n')

        else:
            print('\n')
            for voto in range(len(votiEconomia)): 
                print(votiEconomia[voto]), 

            print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiEconomia))) + '\n')

    elif (materiaSelezionata == 3):
        #controllo se ci sono voti inseriti
        if not votiDiritto:
            print('La materia ' + materie[materiaSelezionata].lower() + ' non ha voti inseriti\n')

        else:
            print('\n')
            for voto in range(len(votiDiritto)): 
                print(votiDiritto[voto]), 

            print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiDiritto))) + '\n')

    elif (materiaSelezionata == 4):
        #controllo se ci sono voti inseriti
        if not votiSociologia:
            print('La materia ' + materie[materiaSelezionata].lower() + ' non ha voti inseriti\n')

        else:
            print('\n')
            for voto in range(len(votiSociologia)): 
                print(votiSociologia[voto]), 

                print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiSociologia))) + '\n')

    else:
        print('C\'è stato un problema durante la visualizzazione dei voti, riprovare per piacere\n')


while True:
    inizializzaScript()