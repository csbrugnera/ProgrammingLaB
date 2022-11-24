#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#venga inizializzato sul nome del file csv, e
#abbia un attributo “name” che ne contenga il nome
#abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
#Provatelo sul file “shampoo_sales.csv”.
#Poi, committate il file in cui l’avete scritto.

class File()
			def __init__(self, file_name):
					self.name = file_name

			def get_data() #def get_data(file_name)xkè viene usato diciamo
				my_little_list = []  #lista interna
				my_big_list = [] #lista in output
				my_file_opened = open(self.name, 'r')
				for line in my_file_opened:
								my_little_list = line.split(',')
								my_big_list.append(my_little_list)
								print(my_big_list)
			return(my_big_list)

csv_file = File(shampoo_sales.csv)
#ho creato oggetto csv_file tramite lo stampo class file()

#final_list = get_data(shampoo_sales.csv) è sbagliata

final_list = csv_file.get_data() 
#ho creato lista che fa l'azione get_data con file csv_file

#CSVFile.get_data(file_name) xkè l'ho messo prima

  