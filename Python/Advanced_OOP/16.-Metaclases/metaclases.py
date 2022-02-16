#En el enfoque de Python, todo es un objeto y cada objeto tiene algún tipo asociado. Para obtener
#el tipo de cualquier objeto, utilice la función type (). Ejecute el código en el panel derecho para ver la
# función type () en acción.

class Dog:
    pass


age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))

#Podemos ver que los objetos en Python están definidos por sus clases inherentes.
# El ejemplo también muestra que podemos crear nuestras propias clases, y esas clases serán instancias del
# tipo clase especial, que es la metaclase predeterminada responsable de crear clases.
for t in (int, list, type):
    print(type(t))

#Estas observaciones nos llevan a las siguientes conclusiones:
# Las metaclases se utilizan para crear clases;
# Las clases se utilizan para crear objetos;
# El tipo del type de metaclase es type; no, eso no es un error tipográfico.

#          / \           METACLASES
#         / | \               |
#           |                 | es una instancia de: METACLASES
#           |                 |
#           |              CLASES
#           |                 |
#           |                 | es una instancia de: CLASES
#           |                 |
#           |         OBJECTO DE LA CLASE
#
#Para ampliar las observaciones anteriores, es importante agregar:
# Type es una clase que genera clases definidas por un programador;
# Las metaclases son subclases de la clase Type.
#