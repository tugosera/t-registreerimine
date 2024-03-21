import random
import string
import smtplib, ssl

def vivod_polzovatelej(kasutajad, paroolid, mail):
    for i in range(len(kasutajad)):
        print(f"{kasutajad[i]}, {mail[i]}, {paroolid[i]}")

def registreerimine(kasutajad, paroolid, mail):
    nimi = input("Vvedite username: ")
    if nimi not in kasutajad:
        email=input("Sisesta email: ")
        parool_valik = input("Sozdat svoi parol (vedite 'ja') ili sgenerirobat random (vvedite 'ei')? ")
        if parool_valik.lower() == "ja":
            parool = input("vvedite parol: ")
            paroolid.append(parool)
            mail.append(email)
            kasutajad.append(nimi)
            save(nimi, parool, email, "registreerimine.txt")
            print("Vi zaregistrirovalis!")
        else:
            parool = random_parol()
            paroolid.append(parool)
            mail.append(email)
            kasutajad.append(nimi)
            save(nimi, parool, email, "registreerimine.txt")
            print("Vi zaregistrirovalis!")
            print("Novi parol: ", parool)

def autoriseeri_kasutaja(nimi, parool, kasutajad, paroolid):
    if nimi in kasutajad:
        if paroolid[kasutajad.index(nimi)] == parool:
            return True
    return False

def smena_parola(nimi, vana_parool, uus_parool, kasutajad, paroolid):
    if autoriseeri_kasutaja(nimi, vana_parool, kasutajad, paroolid):
        paroolid[kasutajad.index(nimi)] = uus_parool
        return "Parol izmenen"
    return "Oshibka, proverte dannie"

def zabil_parol(nimi, kasutajad, paroolid):
    if nimi in kasutajad:
        indeks = kasutajad.index(nimi)
        uus_parool = random_parol()
        paroolid[indeks] = uus_parool 
        print("Sozdan novi parol: " + uus_parool)
    print("Polzovatela ne naiden")

def random_parol(pikkus=8):
    parool = ''.join(random.choices(string.ascii_letters + string.digits, k=pikkus))
    return parool

def save(uus_user, uus_parool, uus_email, registreerimine):
    save =f"{uus_user}_{uus_parool}:{uus_email}"
    with open (registreerimine, "a") as s:
        s.write(f"{save}\n")

def read_file (file, kasutajad, paroolid, mail):
    with open(file, 'r') as s:
        data = s.readlines()
        if len(data):
            for line in data:
                name_password_and_email = line.strip().split(':')
                email = name_password_and_email[1]
                name_and_password = name_password_and_email[0].split("_")
                name = name_and_password[0]
                password = name_and_password[1]
                kasutajad.append(name)
                paroolid.append(password)
                mail.append(email)

def prislat_parol(to_email, parool):
    from email.message import EmailMessage
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "erik.gerega@gmail.com"
    password = "baqd vgeh msad xbbm "
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(f"vas parol - {parool}")
    msg['Subject'] = "vas parol!"
    msg['From'] = sender_email
    msg['To'] = to_email


    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)

    except Exception as e:
        print(e)
    finally:
        server.quit()
