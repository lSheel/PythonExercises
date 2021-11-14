#El atributo de rastreo  (traceback)
# Cada objeto de excepción posee un atributo __traceback__.
# Python nos permite operar en los detalles de rastreo porque cada objeto de excepción (no solo los encadenados)
# posee un atributo __traceback__. Examinemos un objeto así mientras preparamos nuestro cohete para su lanzamiento.

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))



#Del codigo anterior, podemos concluir que tenemos que lidiar con un objeto de
# tipo traceback. Para lograr esto, podríamos usar el método format_tb () entregado por el módulo de rastreo
# incorporado para obtener una lista de cadenas que describen el rastreo. Podríamos usar el método print_tb (),
# también entregado por el módulo de rastreo, para imprimir cadenas directamente en la salida estándar.




import traceback

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')
