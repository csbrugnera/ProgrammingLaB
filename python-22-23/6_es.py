#==============================
#  Classe per file CSV
#==============================

#Esercizio
#Modificate l’oggetto CSVFile della lezione precedente in modo che alzi un'eccezione se il nome del file non è una stringa (nell’ __init__() ).
#Poi, modificate la funzione get_data() di CSVFile in modo da leggere solo un’ intervallo di righe del file*, aggiungendo gli argomenti start ed end opzionali, controllandone la correttezza e sanitizzandoli se serve.
#get_data(self, start=None, end=None)
#*inclusa l’intestazione, estremi inclusi, e partendo da “1”.
#Alla fine ricordatevi di committare tutto


class CSVFile:

    def __init__(self, name):
        
        self.name = name

        if not isinstance(name, str):
          raise Exception
          print('Ho avuto un errore')
          return False
        
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e: #se non può leggere
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self, start=None, end=None):

        if not self.can_read:
            
            # Se nell'init ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            
            # Esco dalla funzione tornando "niente".
            return None

        else:
            #i = start #contatore di righe
            data = [] #Lista vuota per salvare tutti i dati
            estremi = [start, end] #setto le linee che voglio leggere
          
            if start>end: #casistica in cui utente ha invertito
                raise Exception ('Il numero iniziale non può essere maggiore del finale')
                return None
          
    
            my_file = open(self.name, 'r') #apro il file in lettura

            i=1
            for line in my_file: # Leggo il file linea per linea
                if i>= start and i<=end:
                    elements = line.split(',') #faccio split di ogni riga
                    elements[-1] = elements[-1].strip() #pulisco carattere newline
    
                # Se NON sto processando l'intestazione...
                    if elements[0] != 'Date':
                        data.append(elements) #Aggiungo alla lista gli elementi di questa linea
                        print (line)
                        i = i + 1
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data

File_run = CSVFile('shampoo_sales.csv')
data=File_run.get_data(28, 29)

