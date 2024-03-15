from registracija_module import * 
kasutajad=[]
parolid=[]
da=0
while True:
    vibor1=int(input(" 1-log in \n 2-sign in \n"))
    if vibor1==1:
        log_in(kasutajad,parolid)
    elif vibor1==2:
        sign_in(kasutajad,parolid)
    elif vibor1==3:
        info(kasutajad,parolid)
    if da==1:
        break
print("uraaaaaaa!!!")
