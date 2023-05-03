from random import shuffle

def generateur(n):
    l_croissante = [k for k in range(n)]
    l_decroissante = [k for k in range(n-1,-1,-1)]
    l_non_triee = [k for k in range(n)]
    shuffle(l_non_triee)
    
    return [l_croissante, l_decroissante, l_non_triee]

def permutation(tab,i1,i2):
    tmp = tab[i1]
    tab[i1] = tab[i2]
    tab[i2] = tmp
    return tab

def insertion(tab,index,val):
    tab.insert(index,val)
    return tab

def tri_insertion(args):
    ret = []
    for tab in args:
        for i in range(1,len(tab)):
            j=i
            while j>0 and tab[j]<tab[j-1]:
                tab = permutation(tab,j,j-1)
                j-=1
        ret.append(tab)
    return ret


def tri_selection(args):
    ret = []
    for tab in args[1:]:
        for n in range(len(tab)):
            tab = permutation(tab,n,tab.index(min(tab[n:])))
        ret.append(tab)
    return ret
    
print(tri_insertion(generateur(100)))