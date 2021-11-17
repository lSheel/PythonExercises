try:
    import abcdefghijk

except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)
#La excepción ImportError:
# se genera cuando la declaración de importación tiene problemas al intentar cargar un módulo. Los atributos son:
# nombre: representa el nombre del módulo que se intentó importar;
# ruta: representa la ruta a cualquier archivo que haya desencadenado la excepción, respectivamente. Podría ser Ninguno.