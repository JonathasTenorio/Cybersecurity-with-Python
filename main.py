import os
import platform

system_info = platform.uname()

if system_info[0] == "Windows":

    diretorio_pai = '../Ferramentas/' 


    diretorios = [ d for d in os.listdir(diretorio_pai) if os.path.isdir(os.path.join(diretorio_pai, d))]

    print("Scripts")
    x = 0
    for diretorio in diretorios:
        print(str(x)+ " - " + diretorio)
        x +=1
else:

    print("""Este sistema de gerenciamento só esta disponível no momento para Windows. . . 

            Você ainda pode acessar as ferramentas de modo manual . . .                """)
    



    
