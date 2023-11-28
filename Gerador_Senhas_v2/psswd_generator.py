import argparse
import random
import string
import zipfile
import tarfile

alpha = string.ascii_letters
num = string.digits
espc = '! @#$%¨&*()-_=+§ªº/?°;:.>,<'
parser = argparse.ArgumentParser(description="GERADOR DE SENHAS RANDOMICAS!")
parser.add_argument('-s', '--size', type=int, help='Quantidade de caracteres que tera a senha gerada.', default=8)
parser.add_argument('-a', '--alpha', help='Utiliza apenas letras para gerar a senha.', default=alpha)
parser.add_argument('-f', '--file', help='Nome da wordlist. Se nao especificado ira utilizar a wordlist no diretório '
                                         'atual.', default='a.txt.tar')
args = parser.parse_args()


def gerador(chars, size, path):
    if '.zip' in path:
        z = zipfile
        print('Descomprimindo arquivo . . . . .')
        descompac(path, z)
    elif '.tar' in path:
        t = tarfile
        print('Descomprimindo arquivo . . . . .')
        descompac(path, t)
    with open(path, "r", encoding="ISO-8859-1") as file:
        print("Gerando a senha . . . .")
        rand = random.SystemRandom()
        jst = (''.join(rand.choice(chars) for _ in range(size)))
        print('Sucesso!\nSenha: {}'.format(jst))
        print('Buscando senhas iguais em: {}'.format(path))
        for linha in file:
            linhas = linha.strip()
            if jst == linhas:
                print("É igual: " + jst + " A string do arquivo é: " + linhas)
                gerador(chars=args.alpha, size=args.size, path=args.file)

    print("Sucesso! A sua senha não é igual a nenhuma outra neste arquivo.")



def descompac(file, tipo):
    try:
        tipo.open(file, 'r')
        tipo.extractall()
        tipo.close()
        file = file.strip(tipo)
        print(file)
        gerador(chars=args.alhpa, size=args.size, path=file)
    except:
        print("Error")



if __name__ == '__main__':
    print('''
	======================================
	|| Gerador e Comparador de Senhas   ||
	|| version 2.0                      ||
	||                                  ||
	|| gs.py -a 'abcde' -s 4            ||
	======================================
	''')
    gerador(args.alpha, args.size, args.file)
