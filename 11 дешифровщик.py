bglas="AEIOUY"
mglas="aeiouy"
f = open('text.txt')
S=""
i=0
symb=f.read(1)
while symb:
    if mglas.find(symb)!=-1:
        S=S+mglas[(mglas.find(symb)+1)%6]
    elif bglas.find(symb)!=-1:
        if bglas.find(symb)== 0:
            S=S+bglas[5]
        else:
            S=S+bglas[bglas.find(symb)-1]
    elif symb==";":
        symb=f.read(1)
        i=ord(symb)
        if symb==";":
            i=31
        S=S+chr(i+32)
    elif symb=="?":
        symb=f.read(1)
        i=ord(symb)
        if symb=="?":
            i=-5
        S=S+chr(i+64)
    else:
        S=S+symb
    symb=f.read(1)    
f=open('text.txt', 'w')
f.write(S)
f.close()
