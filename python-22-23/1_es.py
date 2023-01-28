#scrivere una funzione sum_list che sommi tutti gli elementi di una lista
def sum_list(my_list):
  somma = 0
  for item in my_list: 
    somma = somma + item
    
  return(somma)


my_list = [1, 3, 6, 9]
#somma = 0 non va bene qua perche solo variabili locali!
somma = sum_list(my_list)
print(somma)

