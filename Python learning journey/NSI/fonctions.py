from math import*
def bonjour(nom):
    '''
    affiche bonjour + {nom}
    arguments : nom,str
    sortie : Bonjour {nom} !
    '''
    return(f"Bonjour {nom} !")
def somme(a,b):
    '''
    retourne {a}+{b}
    arguments : a,int or float et b,int or float
    sortie : a+b
    '''
    return(a+b)
def mult(a,b):
    '''
    retourne {a}*{b}
    arguments : a,int or float et b,int or float or float
    sortie : a*b
    '''
    return(a*b)
def carre(a):
    '''
    retourne {a}**2
    arguments : a,int or float
    sortie : a**2
    '''
    return(mult(a,a))
def puissance_n(x,n):
    '''
    retourne {x}**{n}
    arguments : a,int or float et b,int or float
    sortie : x**n
    '''
    return(x**n)
def max2 (*args):
    '''
    retourne max(*args)
    arguments : *args,int or float et b,int or float
    sortie : max(*args)
    '''
    return(max(*args))
def max3 (*args):
    '''
    retourne max2(*args)
    arguments : *args,int or float et b,int or float
    sortie : max2(*args)
    '''
    return(max2(*args))
def calcul_perimetre(a,b):
    '''
    retourne 2{a}+2{b}
    arguments : a,int or float et b,int or float
    sortie : 2(a+b)
    '''
    return(2*(a+b))
def calcul_aire(a,b):
    """
    retourne a*b
    arguments : a,int or float et b,int or float
    sortie : a*b
    """
    return(a*b)
def triangle_rectangle(a,b,c):
    '''
    retourne si le triangle est rectangle ou non
    arguments : a,int or float et b,int or float c,int or float
    sortie : True or False
    '''
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+c**2:
        return(True)
    else:
        return(False)
def calcul_reduction(a,b):
    '''
    retourne le prix final post-reduction
    arguments : a,int or float et b,int or float, en pourcents
    sortie : a-a*(b/100)
    '''
    return a-a*(b/100)
def nb_boites(a):
    '''
    retourne le nombre de boites complètes posssible qvec mes oeufs
    arguments : a,int
    sortie : a//6
    '''
    return a//6
def est_pair (a):
    '''
    retourne si le nombre est pair ou non
    arguments : a,int
    sortie : True OU False, bool
    '''
    if a%2 == 0:
        return True
    return False
def concatenation (a,b):
    '''
    retourne le mix des deux chaines
    arguments : a,str et b,str
    sortie : a+b
    '''
    return a+b
def avoir_longueur (a):
    '''
    retourne la longueur de la chaine
    arguments : a,str
    sortie : len(str),int
    '''
    return len(a)
def longeure_pair (a):
    '''
    retourne si la longueure de la chaine est paire ou non
    arguments : a,str
    sortie : True OU False, bool
    '''
    if avoir_longueur(a)%2 == 0:
        return True
    return False
def contient_e (a):
    '''
    retourne si la chaine contient "e"
    arguments : a,str
    sortie : True OU False, bool
    '''
    if "e" in a:
        return True
    return False
def masquage(a):
    '''
    retourne la chaine en masqué
    arguments : a,str
    sortie : "*"*len(a)
    '''
    return "*"*len(a)
def bin2(a):
    '''
    retourne le binaire du nombre
    arguments : a,int
    sortie : bin(a),int
    '''
    result =  ""
    while a!=0 :
        result = result + str(a%2)
        a = a//2
    return result[-1:0:-1]+ result[0]
def hexa2(a):
    '''
    retourne l' hexa du nombre
    arguments : a,int
    sortie : hexa(a),int
    '''
    result = []
    while a!=0 :
        result.insert(0,a%16)
        a = a//16
        dico = [[10,"a"],[11,"b"],[12,"c"],[13,"d"],[14,"e"],[15,"f"]]
        for i in range(len(result)):
            for x in range(len(dico)):
                if result[i] == dico[x][0]:
                    result[i] = dico[x][1]
    resultat = ""
    for i in result:
       resultat = resultat + str(i)
    return resultat
def aide(fonc):
    '''
    Pour que toute cette doc ais une utilitée :)
    '''
    commandes = ["bonjour","somme","mult","carre","puissance_n","max2", "max3","calcul_perimetre","calcul_aire","triangle_rectangle","calcul_reduction","nb_boites","concatenation","est_pair","avoir_longueur","longeure_pair","contient_e","masquage","bin2"]
    if fonc == "all":
        for i in range(len(commandes)-1):
            print(commandes[i])
    else:
        print(fonc.__doc__)
print("Utilisez aide({fonction}) pour obtenir de l'aide sur une fonction précise, \net aide('all') pour la liste des fonctions")

print(hexa2(4172682))
print(str(hex(4172682))[2:])