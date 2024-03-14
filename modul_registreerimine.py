<<<<<<< HEAD
def registreerimine (p:list,u:list,da:int)->any:
=======
def registreerimine (p:list,u:list,)->any:
>>>>>>> ff96d11946b15f685de2212de7b89f6ac2e63139
    """

    """
    username=input("Vedite username: ")
    parol=input("Vedite parol: ")
<<<<<<< HEAD
    return p,u,da
=======
    return p,u
>>>>>>> ff96d11946b15f685de2212de7b89f6ac2e63139

def vivod_dannih (p:list,u:list,)->any:
    """

    """
    print("usernames: ", u)
    print("passwords: ", p)
    print()
    return p,u

<<<<<<< HEAD
def sign_in (p:list,u:list,da:int,z:int,x:int)->any:
=======
def sign_in (p:list,u:list,)->any:
>>>>>>> ff96d11946b15f685de2212de7b89f6ac2e63139
    """

    """
    username=input("Vedite username: ")
    parol=input("Vedite password: ")
    for i in range(0, len(u)):
        if username==u[i]:
<<<<<<< HEAD
            z=1   
        else: 
            z=0

    for y in range(0, len(p)):
        if parol==p[y]:
            x=1
        else:
            x=0

    if z==1 and x==1:
        print("fffff")
        da=1
    else:
        print("daun")
        da=0
    print()

    return p,u,da,z,x
=======
            for y in range(0, len(p)):
                if parol==p[y]:
                    print("Vi voshli v akaunt")
                else:
                    print("neverni parol")
        else: 
            print("Polzovatel s takim username ne naiden")
    print()
    return p,u
>>>>>>> ff96d11946b15f685de2212de7b89f6ac2e63139


def change (p:list,u:list,)->any:
    """

    """
    username=input("Vedite username: ")
    novij=input("Vedite novij username: ")
    for i in range(0, len(u)):
        if username==u[i]:
            u[i] = novij
    print()
    return p,u

def change2 (p:list,u:list,)->any:
    """

    """
    password=input("Vedite parol: ")
    novij=input("Vedite novij parol: ")
    for i in range(0, len(p)):
        if password==p[i]:
            p[i] = novij
    print()
    return p,u

