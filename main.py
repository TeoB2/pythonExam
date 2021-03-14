import constants
import inserisciVoto
import statistics
from itertools import cycle

#dizionario con le azioni che si possono effettuare
azioni = {
            1: 'Inserisci esame',
            2: 'Vedi voti'
        }

#dizionario con i crediti validi
crediti = {3, 6, 9, 12}

#dizionario contenti i voti delle materie
voti = dict()

def inizializzaScript():
    #inizializzo gli errori a false
    error = False

    #ciclo le aziioni disponibili
    for key,value in list(azioni.items()):
        print("{}) {}".format(key,value))

    #permetto l'input da parte dell'utente
    azioneSelezionata = input("Seleziona un'opzione: ")

    #controllo se l'azione selezionata esiste
    try:
        #sanitizzo l'input che può essere sia un intero che una stringa, per questo motivo controllo se è una stringa
        azioneSelezionata = str(azioneSelezionata).lower()

        #se non è una stringa imposto il flag error a true
        if (type(azioneSelezionata) != str):
            #setto gli errori
            error = True

    except:
            #se non è andato a buon fine il try imposto il flag error a true
            error = True

    #controllo se l'azione inserita esiste (può essere sia l'id dell'azione sia il nome)
    if (not error and (azioneSelezionata == str(constants.ID_AZIONE_INSERISCI_ESAME) or azioneSelezionata == constants.NAME_AZIONE_INSERISCI_ESAME.lower())):
        inserisciEsame()

    elif (not error and (azioneSelezionata == str(constants.ID_AZIONE_VEDI_VOTI) or azioneSelezionata == constants.NAME_AZIONE_VEDI_VOTI.lower())):
        vediVoti()

    else:
        print("Seleziona una azione valida\n")


#permette l'inserimento di un esame
def inserisciEsame():
    error = False

    #richiamo il metodo dove inserisco la materia e mi restituisce il nome della materia (l'input dell'utente) e error (true o false)
    materiaInserita, error = inserisciVoto.inserisciMateria(voti)

    #se ci sono errori stampo un messaggio e blocco l'esecuzione
    if (error):
        print("Inserire il nome della materia e verificare che non sia già stata inserita!")
        return
    
    #effettuo un while così se il numero di crediti è valido vado avanti, altrimenti richiedo il numero di crediti
    while True:
        #richiamo il metodo dove inserisco il numero di crediti e mi restituisce il numero di crediti (l'input dell'utente) e error (true o false)
        creditiMateria, error = inserisciVoto.inserisciCreditiMateria(materiaInserita, crediti)
        
        #se non ci sono errori interrompo il while e vado avanti
        if (not error):
            break

        #se ci sono errori stampo un messaggio
        print('Inserisci un numero di crediti valido!')

    #effettuo un while così se la data dell'esame è valida vado avanti, altrimenti richiedo la data
    while True:
        #richiamo il metodo dove inserisco la data dell'esame e mi restituisce la data (l'input dell'utente) e error (true o false)
        dataEsame, error = inserisciVoto.inserisciDataEsame()

        #se non ci sono errori interrompo il while e vado avanti
        if (not error):
            break

        #se ci sono errori stampo un messaggio
        print('Inserisci una data valida!')

    #effettuo un while così se il voto dell'esame è valido vado avanti, altrimenti lo richiedo
    while True:
        #richiamo il metodo dove inserisco il voto dell'esame e me lo restituisce (l'input dell'utente) e error (true o false)
        votoMateria, error = inserisciVoto.inserisciVotoEsame(materiaInserita)

        #se non ci sono errori interrompo il while e vado avanti
        if (not error):
            break

        #se ci sono errori stampo un messaggio
        print('Il voto inserito deve essere compreso tra ' + str(constants.MIN_VOTO) + ' e ' + str(constants.MAX_VOTO) + '!')
        

    #creo un dizionario con l'esame sostenuto
    dictEsitoMateria = dict()
    dictEsitoMateria["crediti"] = creditiMateria
    dictEsitoMateria["voto"] = votoMateria
    dictEsitoMateria["data"] = dataEsame

    #inserisco al dizionario voti l'esame sostenuto e metto come chiave il nome del corso e poi come un altro dizionario tutti i suoi dati
    voti[materiaInserita] = dictEsitoMateria

    print('È stato inserito l\'esame ' + materiaInserita + ' con una valutazione di ' + str(votoMateria))


#visualizza i voti e la media della materia selezionata
def vediVoti():
    #se non ci sono voti inseriti mostro un errore
    if (not voti):
        print('Non ci sono voti inseriri!')
        return

    #inizializzo delle variabili a 0 utilizzate per calcolare le medie
    numeratorePonderata = 0
    denominatorePonderata = 0
    numeratore = 0
    denomitare = 0

    #ciclo tutti i voti
    for materia in voti:
        #stampo il nome della materia, il numero di crediti, la valutazione e la data dell'esame
        print("Esame: " + str(materia) + " - Crediti: " + str(voti[materia]["crediti"]) + " - Valutazione: " + str(voti[materia]["voto"]) + " - Sostenuto il: " + str(voti[materia]["data"])), 
        
        #mi calcolo il numeratore e il denominatore per effetuare la media ponderata
        numeratorePonderata += (voti[materia]["crediti"] * voti[materia]["voto"])
        denominatorePonderata += voti[materia]["crediti"]

        #aggiungo il voto al numeratore e aggiungo uno al denominatore per calcolare la media aritmetica
        numeratore += voti[materia]["voto"]
        denomitare += 1

    #mi calcolo entrambe le medie
    mediaPonderata = numeratorePonderata / denominatorePonderata
    media = numeratore / denomitare

    #mi stampo le due medie arrotondandole alla seconda cifra decimanle
    print('\nLa tua media ponderata è di ' + str(round(mediaPonderata, 2)))
    print('La tua media artimetica è di ' + str(round(media, 2)))


while True:
    inizializzaScript()