import os


name = input("Introduce un el nombre de la base de datos ") 

os.system('mysqldump -u USERNAME -p DATABASE > ' + name + 'sql')


