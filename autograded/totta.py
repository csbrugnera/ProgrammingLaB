class ExamException(Exception): #classe che gestisce le eccezoni
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):

        time_series = []  #immagazzina le time series di tutto data.csv

        try:
            my_file_opened = open(self.name, 'r')  #provo ad aprire il file gestendo l'eccezione
        except:
            raise ExamException('File illeggibile o inesistente')

        for line in my_file_opened:

            little_list = []  #immagazzina una time series, questa si azzera ogni volta

            try:
                elements = line.strip('\n').split(',')  #verifico che la linea non sia vuota
            except:
                pass

            if len(line) < 2: #una riga non puo' avere meno di due elementi
                pass


            if elements[0] != 'epoch':  #elimino la prima riga di intestazione
                
                try:
                    epoch = int(elements[0])  #converto l'epoch a intero senza gestire l'eccezione
                except:
                    pass

                try:
                    temperature = float(elements[1])  #controllo che la temperatura sia di tipo float
                except:
                    raise ExamException('TypeError, ValueError, FloatingPointError')

                #if not isinstance(epoch, int): #ulteriore controllo sull'epoch
                    #pass

                #if not isinstance(temperature, float): #ulteriore controllo sulla temperatura
                    #pass

                little_list.append((epoch))
                little_list.append((temperature))
                time_series.append((little_list)) #creo la lista di liste


                #devo controllare che siano che gli epoch siano strettamente crescenti
                for i in range(len(time_series) - 1):
                    if time_series[i][0] >= time_series[i + 1][0]:
                        raise ExamException('Epoch non ordinati o duplicati')

        return time_series

def compute_daily_max_difference(time_series):

    if len(time_series) == 0:
        raise ExamException('Errore: time series non puo essere vuota')

    start_epoch = time_series[0][0] - (time_series[0][0] % 86400) #calcolo l'inizio del primo giorno basandomi sul primo elemento della mia prima misurazione
    min = time_series[0][1] #inizializzo il minimo
    max = time_series[0][1] #inizializzo il massimo


    daily_max_difference = [] #inizializzo lista vuota che conterra' le differenze di temperatura di ogni giorno

    count=1 #variabile che controlla se entro nell' if

    for sublist in time_series[1:]: #inizio a considerare le time series dalla seconda sottolista, in quanto la prima l'ho gia' considerata nell'inizializzazione
        
        current_epoch = sublist[0] 
        current_temperature = sublist[1]

        if start_epoch + 86400 > current_epoch:  #current_epoch e start_epoch appartengono sono stesso giorno
            count += 1 #variabile si incrementa e conterra' il numero di iterazioni dello stesso giorno

            if current_temperature > max:
                max = current_temperature

            if current_temperature < min:
                min = current_temperature

        else: #cioe' current_epoch e start_epoch appartengono a giorni idversi

            daily_max_difference.append(max - min if count > 1 else None) #se la variabile count e' rimasta invariata significa che per quel giorno c'e' un'unica misurazione
            start_epoch = sublist[0] - (sublist[0] % 86400)
            count = 1
            min = current_temperature #aggiorno minimo
            max = current_temperature #aggiorno massimo

    if(min > max):
        raise ExamException('Il minimo non puo essere maggiore del massimo')

    daily_max_difference.append(max - min if count > 1 else None) #scrivo anche l'ultima iterazione

    

    return (daily_max_difference)

    
'''
time_series_file = CSVTimeSeriesFile('data.csv') 
time_series = time_series_file.get_data()
valori = compute_daily_max_difference(time_series)
print(time_series) 
'''