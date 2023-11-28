import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('a.txt', atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Arquivo não foi ocultado")