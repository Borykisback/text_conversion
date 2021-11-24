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
    char = False
    char_ = False
    text = str(input("text: "))
    for i in text:
        next = ""
        if (char == True and char_ == True):
                i = i.upper()
                next += i
                #char = False
                #char_ = False
        else:
            if (i.isupper() == True):
                i = i.lower()
                next += i
            else:
                next += i
        x += next
        char = next == "."
        char_ = next == " "
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
        if (isfirst == True): # Мне кажется здесь можно сделать проще, но я не додумался 
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