
'''
fonction that creates a string BWT from the string and a suffixe table

:param string : the text
:param suffixe_table: a suffixe table

:return a string which is the BWT of the input text
'''

def get_btw(string,suffixe_table):
    btw=''
    for index in suffixe_table:
        btw+=string[index-1]
    return btw

def get_n(btw):
    dic=dict()
    for index in range(0,len(btw)):
        if btw[index] not in dic:
            dic[btw[index]]=1
        else:
            dic[btw[index]]+=1
        
    sorted_list=sorted(dic)
    
    n=dict()
    a=0
    for i in sorted_list:
        n[i]=a
        a+=dic[i]
    return n

def get_r(btw):
    dic=dict()
    r=[]
    for index in range(0,len(btw)):
        if btw[index] not in dic:
            dic[btw[index]]=1
            r.append(dic[btw[index]])
        else:
            dic[btw[index]]+=1
            r.append(dic[btw[index]])
    return r 

def left_first(a,k,n):
    return n[a]+k-1


def btw_2_seq(btw,n,r):
    i=0
    t=''
    while btw[i]!="$":
        t = btw[i]+t
        i = left_first(btw[i],r[i],n)
    return t

def first_in_range(a,i,j,btw):
    for l in range(i,j+1):
        if btw[l]==a:
            return l
    return -1

def last_in_range(a,i,j,btw):
    for l in range(j,i-1,-1):
        if btw[l]==a:
            return l
    return -1


def contains(p,btw,n,r):
    i=0
    j=len(btw)-1
    k=len(p)-1
    while k >= 0:
        a = first_in_range(p[k],i,j,btw)
        if a == -1:
            return False
        b= last_in_range(p[k],i,j,btw)
        k-=1
        i=left_first(btw[a],r[a],n)
        j=left_first(btw[b],r[b],n)
    return True


def nb_occurence(p,btw,n,r):
    i=0
    j=len(btw)-1
    k=len(p)-1
    while k >= 0:
        a = first_in_range(p[k],i,j,btw)
        if a == -1:
            return 0
        b= last_in_range(p[k],i,j,btw)
        k-=1
        i=left_first(btw[a],r[a],n)
        j=left_first(btw[b],r[b],n)
    
    return j-i+1


def all_occurence(p,btw,n,r,sa):
    i=0
    j=len(btw)-1
    k=len(p)-1
    while k >= 0:
        a = first_in_range(p[k],i,j,btw)
        if a == -1:
            return []
        b= last_in_range(p[k],i,j,btw)
        k-=1
        i=left_first(btw[a],r[a],n)
        j=left_first(btw[b],r[b],n)
    
    return sa[i:j+1]