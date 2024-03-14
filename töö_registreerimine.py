from modul_registreerimine import *
<<<<<<< HEAD
parol=["1337","228","1488","696969"]
user=["Evgenij","TurboKiller","tugosera","Nikita"]
da=int
z=int
x=int

while True:
    print("1-log in\n 2-sign in\n")
    valik1=int(input())
    if valik1==1:
        registreerimine(parol,user,da)
    elif valik1==2:
        sign_in(parol,user,da,z,x)
    if da==1:
        while True:
            print("Vali mida teha\n 0-posmotret vse username/paroli\n 1-change username\n 2-change password\n")
            valik2=int(input())
            if valik2==0:
                vivod_dannih(parol,user)
            elif valik2==1:
                change(parol,user)
            elif valik2==2:
                change2(parol,user)
        """
        print("Vali mida teha\n 0-posmotret vse username/paroli\n 1-log in\n 2-sign in\n 3-change username\n 4-change password\n")
=======
parol=[1337,228,1488,696969]
user=["Evgenij","TurboKiller","tugosera","Nikita"]

while True:
    print("Vali mida teha\n 0-posmotret vse username/paroli\n 1-log in\n 2-sign in\n 3-change username\n 4-change password\n")

    valik=int(input())
    if valik==0:
        vivod_dannih(parol,user)
    elif valik==1:
        registreerimine(parol,user)
    elif valik==2:
        sign_in(parol,user)
    elif valik==3:
        change(parol,user)
    elif valik==4:
        change2(parol,user)
        """
        dplj cluh drnm exef 
>>>>>>> ff96d11946b15f685de2212de7b89f6ac2e63139
        """

