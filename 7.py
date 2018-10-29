alp="abcdefghijklmnopqrstuvwxyz"
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def CaesarCipherChar(c,k):
    if alp.find(c)!=-1:
        if alp.index(c)+k>25:
            a=alp[(alp.index(c)+k)%26]
        else:
            a=alp[alp.index(c)+k]
    elif  alph.find(c)!=-1:
        if alph.index(c)+k>25:
            a=alph[(alph.index(c)+k)%26]
        else:
            a=alph[alph.index(c)+k]       
    else:
        a=c
    return a
def CaesarCipher(S,k):
    S1=""
    i=0
    while i < len(S):
        S1=S1+CaesarCipherChar(S[i],k)
        i+=1
    return S1
S=input("Введите строку латинских букв: ")
k=int(input("Введите величину сдвига: "))
k=k%26
print(CaesarCipher(S,k))
