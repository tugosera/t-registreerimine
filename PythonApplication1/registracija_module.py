def info(k:list,p:list,da:int)->any:
    """

    """
    print("kasutajad: ", k)
    print("parolid: ", p)
    print(da)


def log_in(k:list,p:list,da:int)->any:
    """

    """
    username=input("Vvedite username: ")
    parol=input("Vvedite parol: ")
    k.append(username)
    p.append(parol)
    da=1
    return k,p,da



def sign_in():
    """

    """
