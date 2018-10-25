bsogl="BCDFGHJKLMNPQRSTVWXZ?"
msogl="bcdfghjklmnpqrstvwxz;"
bglas="AEIOUY"
mglas="aeiouy"
f = open('text.txt')
S=""
i=0
symb=f.read(1)
while symb:
    if bglas.find(symb)!=-1:
        S=S+bglas[(bglas.find(symb)+1)%6]
    elif mglas.find(symb)!=-1:
        if mglas.find(symb)== 0:
            S=S+mglas[5]
        else:
            S=S+mglas[mglas.find(symb)-1]
    elif bsogl.find(symb)!=-1:
        i=ord(symb)
        if bsogl.find(symb)==20:
            i=91
        S=S+";"+chr(i-32)
    elif msogl.find(symb)!=-1:
        i=ord(symb)
        if msogl.find(symb)==20:
            i=127
        S=S+"?"+chr(i-64)
    else:
        S=S+symb
    symb=f.read(1)    
f=open('text.txt', 'w')
f.write(S)
f.close()
