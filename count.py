
def concate_profile(profile_1, profile_2):
    p1 = len(profile_1)
    p2 = len(profile_2)
    pr = [0]*(max(p1,p2))
    for i in range(min(p1,p2)):
        pr[i] = profile_1[i]+profile_2[i]
    if(p1 > p2):
        for i in range(p2,p1):
            pr[i] = profile_1[i]
    elif(p2 > p1):
        for i in range(p1,p2):
            pr[i] = profile_2[i]
    

def somme_profile(profile,i,k):
    som = 0
    for j in range(i,k+1):
        som = som+profile[j]
    return som

def e_k(k):
    l    = [0]*(k+1)
    l[k] = 1
    return l

def count (n,profile,s):
    d = {}
    k = len(profile)

    if n == 0 :
        som = somme_profile(0,k-1)
        S = som*(som-1)
        if S > 0:
            d = {e_k(k):S}
    else:
        for i in range(n):
            d_0 = {}
            if i == 0:
                d_0 = {0:somme_profile(profile,0,k-1)}
            else:
                for k_0 in range(1,k):
                    d_0.union( count(i, profile[:k-1], profile[k-1]) )
            for (l,w_0) in d_0:
                d_1 = {}
                pp  = concate_profile(profile,l)
                if n-1-i == 0:
                    d_1.union({0:(-1 + somme_profile(pp,0,k-1))})
                else:
                    for k_1 in range(1,k):
                        d_1.union(count(n-1-i,pp[:k_1-1],pp[k_1-1]))
                for (r,w_1) in d_1:
                    w = w_0*w_1
                    t = concate_profile( concate_profile(l,r), e_k(k))
                    if t in d:
                        d[t] = d[t] + w
                    else:
                        d.union({t:w})
    return d

