class Demo:
    class_var = 'shared variable'


d1 = Demo()
d2 = Demo()

# both instances allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance variable
print('contents of d1:', d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"

# d1 object owns the variable named 'class_var' which holds a different value than the class variable named in the same way
print('contents of d1:', d1.__dict__)
print(d1.class_var)
print('.' * 20)

# d2 object variables were not influenced
print('contents of d2:', d2.__dict__)

# d2 object variables were not influenced
print('contents of class variable accessed via d2:', d2.class_var)


########################################################################################################
class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    def quack(self):
        print('quacks')


class Chicken:
    species = 'chicken'

    def walk(self):
        pass

    def cluck(self):
        print('clucks')


duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('So many ducks were born:', Duck.counter)

for poultry in duckling, drake, hen, chicken:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()


####################################################
class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))
