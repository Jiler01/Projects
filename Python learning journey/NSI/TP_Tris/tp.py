from random import shuffle
from time import time

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

def tri_insertion(tab):
    for i in range(len(tab)):
        j=i
        while j>0 and tab[j]<tab[j-1]:
            tab = permutation(tab,j,j-1)
            j-=1
    return tab


def tri_selection(tab):
    def minI(tab,n):
        mini = n
        for i in range(n,len(tab)):
            if tab[i]<tab[mini]: mini = i
        return mini

    for n in range(len(tab)):
        tab = permutation(tab,n,minI(tab,n))
    return tab

def tri_bulle(tab):
    for tour in range(len(tab)):
        for el in range(len(tab)-1-tour):
            if tab[el]>tab[el+1]: tab = permutation(tab,el,el+1)
    return tab

def quicksort(tab):
    def rec(tab):
        pivot = len(tab)-1
        ret = pivot
        i = 0
        j = 0
        while i < pivot:
            if tab[i]<=tab[pivot]: 
                j +=1
                if tab[i] > tab[j] : tab = permutation(tab,i,j)
                if i == pivot: ret = j
            i +=1
        return tab, ret
    return rec(tab)


def test_selection():
    l1,l2,l3 = generateur(10)
    print(tri_selection(l1))
    print(tri_selection(l2))
    print(tri_selection(l3))

def test_insertion():
    l1,l2,l3 = generateur(10)
    print(tri_insertion(l1))
    print(tri_insertion(l2))
    print(tri_insertion(l3))

def test_bulle():
    l1,l2,l3 = generateur(10)
    print(tri_bulle(l1))
    print(tri_bulle(l2))
    print(tri_bulle(l3))

def test_quicksort():
    l1,l2,l3 = generateur(10)
    print(quicksort(l1))
    print(quicksort(l2))
    print(quicksort(l3))

test_quicksort()