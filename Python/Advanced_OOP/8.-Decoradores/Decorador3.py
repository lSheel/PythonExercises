#La función pack_books se ejecutará de la siguiente manera:
# la función warehouse_decorator ('kraft') devolverá la función de envoltura;
# la función de envoltura devuelta tomará la función que se supone que decorará como argumento;
# la función contenedora devolverá la función internal_wrapper, que agrega nueva funcionalidad
# (visualización de material) y ejecuta la función decorada.


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
