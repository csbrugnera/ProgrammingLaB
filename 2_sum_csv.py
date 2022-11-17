#scrivere una funzione sum_csv(file_name) che sommi tutti i valori
# delle vendite degli shampoo del file "shampoo_sales.csv"
# committare e autograding

def sum_csv(my_file):
    somma = 0
    my_file = open('shampoo_sales.csv', 'r')
    for line in my_file:
        list = line.split(',') è una lista con due valori
        number = list[1] #ho preso secondo elemento di list (numero)
        somma += number
    return(somma)

#copiare file dentro replit e chiamare la funzione sotto

somma = sum_csv('shampoo_sales.csv')