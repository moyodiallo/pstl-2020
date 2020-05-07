B = [1]

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


def enum_BDD(n,profile,s):
    d = {}
    k = len(profile)

    if n == 1 :
        som = sum(profile,0,k-1)
        S = (som*(som-1)) - s
        if S > 0:
            d = { tuple(e_k(k)):S}
    else:
        for i in range(n):
            d_0 = {}
            if i == 0:
                d_0 = {():sum(profile,0,k-1)}
            else:
                for k_0 in range(1,k):
                    d_0.update( enum_BDD(i, profile[:k_0], profile[k_0]) )
            for (l,w_0) in d_0.items():
                d_1 = {}
                pp  = sum_profile(profile,list(l))
                if n-1-i == 0:
                    d_1.update({():(-1 + sum(pp,0,k-1))})
                else:
                    for k_1 in range(1,k):
                        d_1.update(enum_BDD(n-1-i,pp[:k_1],pp[k_1]))
                for (r,w_1) in d_1.items():
                    w = w_0*w_1
                    t = sum_profile(sum_profile(l,list(r)), e_k(k))
                    if tuple(t) in d.keys():
                        d[tuple(t)] = d[tuple(t)] + w
                    else:
                        d.update({tuple(t):w})
    return d
def enum(nb):
    pool_profile = list()
    pool_profile.append(2)
    
    for i in range(nb-1):
        pool_profile.append(0)
    dico = enum_BDD(nb,pool_profile,0)
    for tree in dico.values():
        B.append(tree)
    return B
print(enum(4))
