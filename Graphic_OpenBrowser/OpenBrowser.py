from tkinter import *
import webbrowser

# Nome da tela (Tela sem nome no caso
root = Tk()

# O título que fica na borda da janela
root.title('Abrir browser')
# Tamanho do sistema (tela)
root.geometry('300x200')


def google():
    webbrowser.open('www.google.com')


Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()
