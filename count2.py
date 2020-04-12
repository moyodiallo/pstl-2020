#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum(T,i,k):
    """Fonction qui somme les entiers du Tableau T
    
    Arguments:
        T {integer} -- Un tableau
        i {integer} -- indice i, souvent egale a 0
        k {integer} -- indice k, limite dans T et k inclu
    
    Returns:
        integer -- un entier
    """
    sum = 0
    for j in range(i,k+1):
        sum = sum + T[j]
    return sum

def sum_profile(T_1,T_2):
    """Fait la somme par indice commun des elements des 2 tableaux
    
    Arguments:
        T_1 {array} -- Le tableau representant le pool profile 1
        T_2 {array} -- Le tableau representant le pool profile 2

    Returns:
        array -- Le resultat de la somme des pool profile dont la longueur max des 2
    """
    p1 = len(T_1)
    p2 = len(T_2)
    Tr = [0]*(max(p1,p2))

   
    if p1 == 0 :
        return T_2
    
    if p2 == 0:
        return T_1

    for i in range(min(p1,p2)):
        Tr[i] = T_1[i]+T_2[i]
    if(p1 > p2):
        for i in range(p2,p1):
            Tr[i] = T_1[i]
    elif(p2 > p1):
        for i in range(p1,p2):
            Tr[i] = T_2[i]
    return Tr



def e_k(k):
    """ Un profile avec k element e^k(n) = (0........1) dont len(0........1) = n
    
    Arguments:
        k {integer} -- le nombre d'element
    
    Returns:
        array -- retourn le profile
    """
    l    = [0]*(k+1)
    l[k] = 1
    return l


def count (n,profile,s):
    """ L'algorithme de comptage
    
    Arguments:
        n {integer}     -- taille du spine a construire
        profile {array} -- la pool profile de debut
        s {integer}     -- level set rank(sibling rank)
    
    Returns:
        array -- Un tableau de couple (p,w). p est profile,w le poid du profile
    """
    d = {}
    k = len(profile)

    if n == 1 :
        som = sum(profile,0,k-1)
        S = (som*(som-1)) - s
        if S > 0:
            d = {tuple(e_k(k)):S}
    else:
        for i in range(n):
            for k_0 in range(1,k):
                if i == 0:
                    (l,w_0) = {((),sum(profile,0,k-1))}
                else:
                    (l,w_0) = count(i, profile[:k_0], profile[k_0])
                pp  = sum_profile(profile,list(l))
                for k_1 in range(1,k):
                    if n-1-i == 0:
                        (r,w_1) = ((),(-1 + sum(pp,0,k-1)))
                    else:
                        (r,w_1) = count(n-1-i,pp[:k_1],pp[k_1])
                        w = w_0*w_1
                        t = sum_profile(sum_profile(l,list(r)), e_k(k))
                        if tuple(t) in d.keys():
                            d[tuple(t)] = d[tuple(t)] + w
                        else:
                            d.update({tuple(t):w})
    return d
print(count(3,[2,0,0],0))
