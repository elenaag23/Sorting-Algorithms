import random
import sys
import time

def merge(s,d):
    new=[]
    i=0
    j=0
    while i<len(s) and j<len(d):
        if s[i]<d[j]:
            new.append(s[i])
            i+=1
        else:
            new.append(d[j])
            j+=1
    new+=s[i:]
    new+=d[j:]
    return new

def merge_sort(v):
    if len(v)==1:
        return v
    mijl=len(v)//2
    st=merge_sort(v[:mijl])
    dr=merge_sort(v[mijl:])
    return merge(st,dr)


def shell_sort(v):
    salt=len(v)//2
    while salt>0:
        i=salt
        while i<len(v):
            elem=v[i]
            j=i
            while v[j-salt]>elem and j>=salt:
                v[j]=v[j-salt]
                j=j-salt
            v[j]=elem
            i+=1
        salt//=2
    return v

def counting_sort(v):
    M = max(v)
    vec=[0 for x in range(len(v))]
    frecv=[0 for x in range(M+1)]
    for x in v:
        frecv[x]+=1
    for i in range(1,M+1):
        frecv[i]+=frecv[i-1]
    i=0
    while i<=len(v)-1:
        if frecv[v[i]]!=0:
            frecv[v[i]]-=1
            vec[frecv[v[i]]]=v[i]
        i+=1
    return vec

def counting_sort_for_radix_b(v,p):
    vec=[0 for x in range(len(v))]
    frecv=[0,0]
    for x in v:
        frecv[(x>>p)&1]+=1
    frecv[1]+=frecv[0]
    i=len(v)-1
    while i>=0:
        if frecv[(v[i]>>p)&1]!=0:
            frecv[(v[i]>>p)&1]-=1
            vec[frecv[(v[i]>>p)&1]]=v[i]
        i-=1
    return vec

def radix_sort(v):
    M=len(bin(max(v)))
    i=1
    p=0
    l=[]
    while i<=M:
        l = counting_sort_for_radix_b(v,p)
        i+=1
        p+=1
        v=l
    return l

def counting_sort_for_radix_16(v,p):
    vec=[0 for x in range(len(v))]
    frecv=[0 for x in range(16)]
    for x in v:
        frecv[(x>>p)&15]+=1
    for i in range(1,16):
        frecv[i]+=frecv[i-1]
    i=len(v)-1
    while i>=0:
        if frecv[(v[i]>>p)&15]!=0:
            frecv[(v[i]>>p)&15]-=1
            vec[frecv[(v[i]>>p)&15]]=v[i]
        i-=1
    return vec

def radix_sort_b16(v):
    M=len(bin(max(v)))
    p=0
    l=[]
    while p<=M:
        l = counting_sort_for_radix_16(v,p)
        p+=4
        v=l
    return v

def divide(v,st,dr):
    pivot_choice=[v[st],v[dr],v[(dr+st)//2]]
    M=max(pivot_choice)
    m=min(pivot_choice)
    if v[st]!=M and v[st]!=m:
        pivot=v[st]
        swap=v[st]
        v[st]=v[dr]
        v[dr]=swap
    elif v[dr]!=M and v[dr]!=m:
        pivot=v[dr]
    else:
        pivot=v[(dr+st)//2]
        pivot = v[(dr+st)//2]
        swap = v[(dr+st)//2]
        v[(dr+st)//2] = v[dr]
        v[dr] = swap
    i=st-1
    j=st
    while j<dr:
        if v[j]<v[dr]:
            i+=1
            swap=v[i]
            v[i]=v[j]
            v[j]=swap
        j+=1
    i+=1
    swap=v[i]
    v[i]=v[dr]
    v[dr]=swap
    return (i,v)

def quicksort(v, val_min, val_max):
    if val_min <= val_max:
        pivot=divide(v, val_min,val_max)
        piv=pivot[0]
        v=pivot[1]
        quicksort(v,val_min,piv-1)
        quicksort(v,piv+1,val_max)
    return v



def sorteaza(v,sort):
    s=sorted(v)
    l=[]
    if sort==0:
        l=merge_sort(v)
    if sort==1:
        l=shell_sort(v)
    if sort==2:
        l=counting_sort(v)
    if sort==3:
        l=radix_sort(v)
    if sort==4:
        l=radix_sort_b16(v)
    if sort==5:
        l=quicksort(v,0,len(v)-1)


sys.setrecursionlimit(10**7)

teste=[(1000,10000000),(10000,1000000),(100000,1000000),(1000000,1000),(10000000,100000)]
sortari=["Merge Sort", "Shell Sort", "Counting Sort", "Radix Sort cu baza 2", "Radix Sort cu baza 16", "Quick Sort"]
v=[]


for test in teste:
    for i in range(test[0]):
        x = random.randint(1, test[1])
        v.append(x)

    for i in range(6):
        start=time.time()
        sorteaza(v,i)
        stop=time.time()
        print(f"{sortari[i]} executata in {stop-start:.4f} secunde, avand N={test[0]} si M={test[1]}.")


