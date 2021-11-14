class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

#en la clase usamos el motodo __Add__ para indicar que si se sumas dos objetos persona, va a sumar el peso
#indicado más el del otro objeto
print(p1 + p2)
