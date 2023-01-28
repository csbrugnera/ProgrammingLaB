#Esercizio (a)
#Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore* se si cerca di aprire un file non esistente.
#Potete fare questo controllo:
#a) nella funzione get_data(), oppure
#b) nell’ __init__() (basta che leggiate la prima riga per vedere se il file esiste)
# *il messaggio di errore deve contenere la parola “Errore” per essere rilevato dal testing.

class File():

    def __init__(self, file_name):
        self.name = file_name

    def get_data(File): #ho aggiunto file
        try:
            my_little_list = []  
            my_big_list = [] 
            my_file_opened = open(self.name, 'r')
            for line in my_file_opened:
                my_little_list = line.split(',')
                my_big_list.append(my_little_list)
                print(my_big_list)
            return(my_big_list)

        except Exception as e:
             print('Ho un errore generico')
             print('Errore di tipo {}' .format(e))

csv_file = File('shampoo_sales.csv')
final_list = csv_file.get_data() 
