import string
import time
from typing import ValuesView

def menu():
    print("(1) Из [а] в [А]\n(2) Из [A] в [a]")
    formenu = str(input("Take: "))
    if formenu == "1":
        from_a_at_A()
    if formenu == "2":
        from_A_at_a()
    if formenu == "3":
        from_()
    else:
        print("What?")
        menu()

def from_a_at_A(): # Конвертировать из мал. в больш.
    x = ""
    text_l = str(input("text: "))
    for up in text_l: 
        if (up.islower() == True):
            up = up.upper()
            x += up
        else:
            x += up
    print(x)
    time.sleep(2)
    menu()

def from_A_at_a(): # Конвертировать из больш. в мал.
    x = ""
    text = str(input("text: "))
    for i in text: 
        if (i.isupper() == True):
            i = i.lower()
            x += i
        else:
            x += i
    print(x)
    time.sleep(2)
    menu()

def from_(): # Функция слишком сделана через заднее место, нужно както переделать
    text = input("text: ")
    ispace = False
    isfirst = True
    newtext = ""
    for i in text:
        temporary = ''
        if (i == text[0] and isfirst == True): # Мне кажется здесь можно сделать проще, но я не додумался 
            i = i.upper()
            isfirst = False
        if (ispace):
            temporary = i.upper()
        else:
            temporary = i       
        newtext += temporary
        ispace = i == ' '
    print(newtext)
        

menu()