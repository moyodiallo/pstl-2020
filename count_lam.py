#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

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
        T_1 {array} -- Le tuple representant le pool profile 1
        T_2 {array} -- Le tuple representant le pool profile 2

    Returns:
        array -- Le resultat de la somme des pool profile dont la longueur max des 2
    """
    p1 = len(T_1)
    p2 = len(T_2)
    Tr = [0]*(max(p1,p2))

    if p1 == 0 :
        return tuple(T_2)
    
    if p2 == 0:
        return tuple(T_1)

    for i in range(min(p1,p2)):
        Tr[i] = T_1[i]+T_2[i]
    if(p1 > p2):
        for i in range(p2,p1):
            Tr[i] = T_1[i]
    elif(p2 > p1):
        for i in range(p1,p2):
            Tr[i] = T_2[i]
    return tuple(Tr)

def e_k(k):
    """ Un profile avec k element e^k(n) = (0........1) dont len(0........1) = n
    
    Arguments:
        k {integer} -- le nombre d'element
    
    Returns:
        array -- retourn le profile
    """
    l    = [0]*(k+1)
    l[k] = 1
    return tuple(l)
    
#On unie deux dictionnaires si une cle se retrouve dans les deux dictionnaires on fait la somme de leurs elements
def union_dic(dic1, dic2):
  dicr={}
  for key in dic1:
    if key in dic2:
      dicr[key]=dic1[key]+dic2[key]
    else:
      dicr[key]=dic1[key]
  for key in dic2:
    if not key in dic1:
      dicr[key]=dic2[key]
      
  
  return dicr
      
      


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

    """On a effectué une legere modification sur l'algorithme dans le cas ou n==0 on ne prend pas en compte cet arbre
        et dans le cas ou n==1 on calcul normalement"""

    if n == 1 :
        som = sum(profile,0,k-1)
        S = som*(som-1)-s
        if S > 0:
            d = {e_k(k):S}
    else:
        for i in range(n):
            d_0 = {}
            if i == 0:
              d_0 = {():sum(profile,0,k-1)}
            else:
                for k_0 in range(1,k):
                    d_0 = union_dic(d_0, count(i, profile[:k_0], profile[k_0]) )
            for (l,w_0) in d_0.items():
                d_1 = {}
                pp  = sum_profile(profile,l)
                if n-1-i == 0:
                    d_1 = union_dic(d_1,{():(-1 + sum(pp,0,k-1))})
                else:
                    for k_1 in range(1,k):
                        d_1 = union_dic(d_1,(count(n-1-i,pp[:k_1],pp[k_1])))
                for (r,w_1) in d_1.items():
                    w = w_0*w_1
                    t = sum_profile( sum_profile(l,r), e_k(k))
                    if t in d:
                        d[t] = d[t] + w
                    else:
                        d[t]=w
    return d

if len(sys.argv)<3:
    print("Le format est python3 count.py [nombre de noeud de la bdd] [nombre de variables]")
else:
  print(count(int(sys.argv[1]),tuple([2]+[0]*(int(sys.argv[2])-1)),0))
