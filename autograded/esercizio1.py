#Scrivete una funzione
#sum_list(my_list)
#che sommi tutti gli elementi di una lista.

def sum_list(my_list):
    sum = 0
    
    if len(my_list) == 0:
        return None
        
    for item in my_list:
        sum = sum + item
    return sum