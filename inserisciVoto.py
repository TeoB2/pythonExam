import constants
import datetime
from datetime import date

#inserisce il nome della materia e la restituisce insieme al flag error
def inserisciMateria(voti, error = False):
    #input con il nome della materia
    materiaInserita = input('Inserisci la materia di cui si è sostenuto l\'esame: ')

    try:
        #sanitizzo la stringa e la metto tutta minuscola
        materiaInserita = str(materiaInserita).lower()
        
        #controllo se è una striga, se non è vuota e se non è già inserita la materia nel dizionario voti
        if (type(materiaInserita) != str or len(materiaInserita) == 0 or materiaInserita in voti):
            #setto gli errori
            error = True

    except:
        #setto gli errori
        error = True

    #restituisco il nome della materia inserito e gli eventuali errori
    return materiaInserita, error


#inserisce i crediti della materia e li restituisce insieme al flag error
def inserisciCreditiMateria(materiaInserita, crediti, error = False):
    #input con i crediti della materia
    creditiMateria = input('Inserisci il numero di crediti della materia ' + materiaInserita + ': ')

    try:
        #sanitizzo l'intero
        creditiMateria = int(creditiMateria)

        #controllo se è un intero e se il numero di crediti è valido verificando se è nel dizionario crediti
        if (type(creditiMateria) != int or not creditiMateria in crediti):
            #setto gli errori
            error = True

    except:
        #setto gli errori
        error = True

    #restituisco il numero di crediti della materia e gli eventuali errori
    return creditiMateria, error


#inserisce la data dell'esame e la restituisce insieme al flag error
def inserisciDataEsame(error = False):
    #input con la data dell'esame
    dataEsame = input('Inserisci la data in cui si è sostenuto l\'esame nel formato DD-MM-AAAA: ')

    #se il campo viene lasciato vuoto viene presa la data odierna
    if(len(dataEsame) == 0):
        today = date.today()
        
        dataEsame = today.strftime("%d-%m-%Y")

    #verigico se la data è valida
    try:
        #con uno split prendo il giorno, il mese e l'anno e li metto in 3 variabili
        day, month, year = dataEsame.split('-')

        datetime.datetime(int(year),int(month),int(day))

    except ValueError:
        error = True

    #restituisco la data in cui si è sostenuto l'esame e gli eventuali errori
    return dataEsame, error


#permette l'inserimento della votazione di un esame e lo restituisce insieme al flag error
def inserisciVotoEsame(materiaInserita, error = False):
    #input per chiedere il voto dell'esame
    votoMateria = input('Inserisci il voto della materia ' + materiaInserita + ': ')

    try:
        #sanitizzo l'intero
        votoMateria = int(votoMateria)

        #controllo se è un intero e se il voto è accettabile (tra 18 e 30)
        if (type(votoMateria) != int or votoMateria < constants.MIN_VOTO or votoMateria > constants.MAX_VOTO):
            #setto gli errori
            error = True

    except:
        #setto gli errori
        error = True

    #restituisce la votazione dell'esame e gli eventuali errori
    return votoMateria, error