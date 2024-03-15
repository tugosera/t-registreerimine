from registracija_module import * 
kasutajad=[]
parolid=[]
da=0
while da==0:
    vibor1=int(input(" 1-log in \n 2-sign in \n 3-info\n"))
    if vibor1==1:
        log_in(kasutajad,parolid,da)
    elif vibor1==2:
        sign_in(kasutajad,parolid)
    elif vibor1==3:
        info(kasutajad,parolid,da)
print("uraaaaaaa!!!")
