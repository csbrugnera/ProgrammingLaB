#scrivere una funzione sum_csv(file_name) che sommi tutti i valori
# delle vendite degli shampoo del file "shampoo_sales.csv"
# committare e autograding

def sum_csv(my_file):
    somma = 0
    my_list = []
    my_file_opened = open(my_file, 'r')
    for line in my_file_opened:
        my_list = line.split(',')#è una lista con due valori
        if my_list[0] != 'Date':
            number = float(my_list[1]) #ho preso secondo elem   
            somma += number
      
    return(somma)

#copiare file dentro replit e chiamare la funzione sotto

totale = sum_csv('shampoo_sales.csv')
print(totale)