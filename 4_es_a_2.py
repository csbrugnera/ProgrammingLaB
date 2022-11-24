#PROVO A FARLO MODIFICANDO INIT
class File():

    def __init__(self, file_name):
        try:
            my_file_opened = open(self.name, 'r')
            self.name = file_name
      
        except Exception as e:
            print('Non posso leggere file')
            print('Errore di tipo: {}' .format(e))

    def get_data(): 
        my_little_list = [] 
        my_big_list = []
        my_file_opened = open(self.name, 'r')

        for line in my_file_opened:
            my_little_list = line.split(',')
            my_big_list.append(my_little_list)
            print(my_big_list)
          
        return(my_big_list)

    csv_file = File(shampoo_sales.csv)
    final_list = csv_file.get_data() 