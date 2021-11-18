#El código comienza con la declaración de importación responsable de cargar el módulo pickle:
import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

#puede ver que el identificador de archivo 'file_out' está asociado con el archivo abierto para escribir en modo
# binario. Es importante abrir el archivo en modo binario, ya que volcamos datos como un flujo de bytes.
with open('multidata.pckl', 'wb') as file_out:
    #Ahora es el momento de conservar el primer objeto con la función dump ().
    # Esta función espera que se conserve un objeto y un identificador de archivo.
    pickle.dump(a_dict, file_out)
    #Y el segundo objeto se conserva de la misma manera:
    pickle.dump(a_list, file_out)

#Ahora es el momento de deshacer el contenido del archivo. El código presentado es bastante simple:
# estamos importando un módulo pickle;
# el archivo se abre en modo binario y el identificador de archivo está asociado con el archivo;
# leemos consecutivamente algunas porciones de datos y las deserializamos con la función load ();
# finalmente, examinamos el tipo y contenido de los objetos.

with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)