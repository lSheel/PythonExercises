#Métodos estáticos
# Los métodos estáticos son métodos que no requieren (¡y no lo esperan!)
# Un parámetro que indique el objeto de la clase o la clase en sí para ejecutar su código.
# ¿Cuándo puede ser útil?
# Cuando necesita un método de utilidad que viene en una clase porque está relacionado semánticamente,
# pero no requiere un objeto de esa clase para ejecutar su código; en consecuencia, cuando el método estático
# no necesita conocer el estado de los objetos o clases.

class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
