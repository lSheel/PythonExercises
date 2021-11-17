#Excepciones avanzadas: excepciones encadenadas explícitamente
# Esta vez nos gustaría convertir un tipo explícito de objeto de excepción en otro tipo de objeto de
# excepción en el momento en que se produce la segunda excepción. Imagina que tu código es responsable del
# proceso de verificación final antes de que se lance el cohete. La lista de comprobaciones es larga y distintas
# comprobaciones pueden dar lugar a distintas excepciones. Pero como es un proceso muy serio, debe asegurarse de
# que se aprueben todas las comprobaciones. Si alguno falla, se debe marcar en el libro de registro y volver a
# verificar la próxima vez.


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

personnel_check()