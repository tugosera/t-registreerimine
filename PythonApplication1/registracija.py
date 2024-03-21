import smtplib
import ssl
from email.message import EmailMessage
from registracija_module import *

kasutajad = []
valid = []
paroolid = []
read_file("registreerimine.txt", kasutajad, paroolid, valid)
while True:
    print("Valikud \n 1.Registratsija\n 2.Avtorizatsija\n 3.Smena parola\n 4.ja zabil parol \n 5.Spisok polzovatelei \n 6.Zakonchit \n 7. Otpravka pisma")
    valik = input("Vali tegevus: ")
    if valik == "1":  # Регистрация
        registreerimine(kasutajad, paroolid, valid)
    elif valik == "2":  # Авторизация
        nimi = input("Vvedite username: ")
        parool = input("Vvedite parol: ")
        if autoriseeri_kasutaja(nimi, parool, kasutajad, paroolid):
            print("Vi avtorizovalis")
            print()
        else:
            print("Vi ne avtorizovalis")
            print()
    elif valik == "3":  # Изменить пароль
        nimi = input("Vvedite username: ")
        vana_parool = input("Vvedite stari parol: ")
        uus_parool = input("Vvedite novi parol: ")
        print(smena_parola(nimi, vana_parool, uus_parool, kasutajad, paroolid))
    elif valik == "4":  # Забыли пароль
        nimi = input("Vvedite username: ")
        print(zabil_parol(nimi, kasutajad, paroolid))
    elif valik == "5":  # Просмотр добавленных пользователей
        vivod_polzovatelej(kasutajad, paroolid, valid)
    elif valik == "6":  # Выход
        print("programma zavershilas")
        print()
        break
    elif valik == "7":
        K = input("Vvedite svoi email: ")
        index1 = None
        for index, L in enumerate(valid):
            if L == K:
                index1 = index
                break
        prislat_parol (K,paroolid[index1])
    else:
        print("Neverni vibor")
        print()
