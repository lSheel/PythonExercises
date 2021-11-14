class A:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre


class B(A):
    def __init__(self, apellido):
        super(B, self).__init__("Luis")
        self.__apellido = apellido

    def __str__(self):
        return self.__apellido


class C(B):
    def __init__(self, edad):
        super(C, self).__init__("Gonzalez")
        self.__edad = edad

    def __str__(self):
        a = A.__str__(self) + " " + B.__str__(self) + " " + self.__edad
        return a


c = C("12")
print(c.__str__())

print(issubclass(C, A))
