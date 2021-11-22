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

def from_():
    text = input("text: ")
    ispace = False
    x = ""
    for i in text:
        new_simbol = ' '
        if (ispace):
            new_simbol = i.upper()
        else:
            new_simbol = i       
        x += new_simbol
        ispace = i == ' '
    print(x)
        

menu()