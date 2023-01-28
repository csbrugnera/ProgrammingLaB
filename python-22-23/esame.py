class MovingAverage():
    def __init__(self, factors):
        self.factors = factors

    def compute(self, value_list):
        i = 0 #posizione primo elemento da prendere nella lista
        j = self.factors #posizione ultimo elemento. Faccio "-1" perchè parte da 0
        avg_list = []
        window_range = None

        while j <= len(value_list):
            window_range = value_list[ i : j ] #lista-finestra
            somma = sum(window_range) #faccio somma

            #print(i)
            #print(j)
            #print(window_range)
            #print(i,j)

            avg = somma/self.factors #faccio media
            avg_list.append(avg) #inserisco nella lista delle medie il valorw

            i = i + 1 #incremento i e j per muovermi nella listas
            j = j + 1
            
            #print(avg_list)
        return avg_list
            
    
moving_average = MovingAverage(2)
list = [2, 4, 8, 16]
result_avg = moving_average.compute(list)
print(result_avg)  
        