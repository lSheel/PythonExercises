class Fib:
    # Se crea el constructor del generador
    def __init__(self, nn):
        # Atributos locales n = nn se queda con el valor se inicia i, p1, p2
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    # Metodo para iterar
    def __iter__(self):
        print("Fib iter")
        # Devuelve el objeto
        return self

    # Metodo para pasar al siguiente elemento de la iteración
    def __next__(self):
        # Al momento de llamar el metodo se suma +1 a i
        self.__i += 1
        # Se compara el valor actual de i con el valor dado
        if self.__i > self.__n:
            raise StopIteration
        # Si i contiene 1 o 2 regresa 1
        if self.__i in [1, 2]:
            return 1
        # ret va a sumar los valores de p1 y p2
        ret = self.__p1 + self.__p2
        # p1 y p2 van a tener los valores de p2 y ret respectivamente
        self.__p1, self.__p2 = self.__p2, ret
        # regresa ret
        return ret


class Class:
    # El constructor con parametros n
    def __init__(self, n):
        # Atributo privador que va a ser igual a objeto fib(n)
        self.__iter = Fib(n)

    # Metodo iter donde se imprime el objeto iter
    def __iter__(self):
        print("Class iter")
        return self.__iter;


object = Class(8)

for i in object:
    print(i)
