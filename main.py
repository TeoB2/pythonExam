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
    materiaSelezionata = input("Seleziona la materia:\n")

    #controllo se la materia selezionata è un intero
    materiaSelezionata = int(materiaSelezionata)

    #controllo se la materia selezionata esiste
    if (materiaSelezionata >= 1 and materiaSelezionata <= 4):
        azioneSelezionata = input("Vuoi inserire un voto o vederli?\n")

        #controllo se l'azione selezionata è un intero
        azioneSelezionata = int(azioneSelezionata)

        if (azioneSelezionata == 1):
            votoInserito = input('Inserisci il voto della materia ' + materie[materiaSelezionata].lower() + ':\n')

            #controllo se il voto selezionato è un intero
            votoInserito = int(votoInserito)

            if (votoInserito > 0 and votoInserito <= 30):
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

        #inserire controllo se lista vuota
        elif (azioneSelezionata == 2):
            if (materiaSelezionata == 1):
                for voto in range(len(votiInformatica)): 
                    print(votiInformatica[voto]), 

                print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiInformatica))) + '\n')

            elif (materiaSelezionata == 2):
                for voto in range(len(votiEconomia)): 
                    print(votiEconomia[voto]), 

                print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiEconomia))) + '\n')

            elif (materiaSelezionata == 3):
                for voto in range(len(votiDiritto)): 
                    print(votiDiritto[voto]), 

                print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiDiritto))) + '\n')

            elif (materiaSelezionata == 4):
                for voto in range(len(votiSociologia)): 
                    print(votiSociologia[voto]), 

                    print('\nLa tua media della materia di ' + materie[materiaSelezionata].lower() + ' è di ' + str(float(statistics.mean(votiSociologia))) + '\n')

            else:
                print('C\'è stato un problema durante la visualizzazione dei voti, riprovare per piacere\n')

        else:
            print("L'azione che hai selezionato non esiste\n")

    else:
        print("Seleziona una materia esistente\n")


while True:
    inizializzaScript()