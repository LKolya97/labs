f = open('text.txt')
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cl=0
cw=0
clin=0
symb=f.read(1)
while symb:
    if alph.find(symb)!=-1:
        cl+=1
    elif symb==" ":
        cw+=1
    elif symb=="\n":
        clin+=1
        cw+=1
    symb=f.read(1)
cw+=1
clin+=1
print("Input file contains:")
print(str(cl)+" letters")
print(str(cw)+" words")
print(str(clin)+" lines")
