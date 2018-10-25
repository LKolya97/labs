field = [["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"]]
let="abcdefgh"
f=input("Введите фигуру: ")
S=input("Введите клетку: ")
S1=S[0:1:1]
Sc=S[1:2:1]
Sc=int(Sc)-1
Sb=let.find(S1)

if f=="*":
 if Sc!=0:
    field[7-Sc][Sb]="*"
    if Sc==1:
        field[7-Sc-1][Sb]="+"
        field[7-Sc-2][Sb]="+"
    elif Sc<7:
        field[7-Sc-1][Sb]="+"
elif f=="К":
    print(Sb)
    if (7-Sc+2<=7) and (Sb-1>=0):
        field[9-Sc][Sb-1]="+"
    if (7-Sc-2>=0) and (Sb-1>=0):
        field[5-Sc][Sb-1]="+"
    if (7-Sc+2<=7) and (Sb+1<=7):
        field[9-Sc][Sb+1]="+"
    if (7-Sc-2>=0) and (Sb+1<=7):
        field[5-Sc][Sb+1]="+"
    if (7-Sc+1<=7) and (Sb-2>=0):
        field[8-Sc][Sb-2]="+"
    if (7-Sc-1>=0) and (Sb-2>=0):
        field[6-Sc][Sb-2]="+"
    if (7-Sc+1<=7) and (Sb+2<=7):
        field[8-Sc][Sb+2]="+"
    if (7-Sc-1>=0) and (Sb+2<=7):
        field[6-Sc][Sb+2]="+"      
    field[7-Sc][Sb]="K"
elif f=="С":
    i=Sb-1
    count=1
    while i >= 0:
        if 7-Sc-count>=0:
            field[7-Sc-count][i]="+"
        if 7-Sc+count<=7:
            field[7-Sc+count][i]="+"
        i=i-1
        count+=1
    i=Sb+1
    count=1
    while i <= 7:
        if 7-Sc-count>=0:
            field[7-Sc-count][i]="+"
        if 7-Sc+count<=7:
            field[7-Sc+count][i]="+"
        i=i+1
        count+=1
    field[7-Sc][Sb]="С"
elif f=="Л":
      for i in range(0,8): 
          field[i][Sb]="+"
          field[7-Sc][i]="+"
          i+=1
      field[7-Sc][Sb]="Л"    
elif f=="Ф":
    i=Sb-1
    count=1
    while i >= 0:
        if 7-Sc-count>=0:
            field[7-Sc-count][i]="+"
        if 7-Sc+count<=7:
            field[7-Sc+count][i]="+"
        i=i-1
        count+=1
    i=Sb+1
    count=1
    while i <= 7:
        if 7-Sc-count>=0:
            field[7-Sc-count][i]="+"
        if 7-Sc+count<=7:
            field[7-Sc+count][i]="+"
        i=i+1
        count+=1
    for i in range(0,8): 
          field[i][Sb]="+"
          field[7-Sc][i]="+"
          i+=1
    field[7-Sc][Sb]="Ф"      
else:
    print("Введите фигуру корректно")
for i in range(0, 8):
    for j in range(0, 8):
        print(field[i][j], end=" ")
        j+=1    
    
    print()    
    i+=1

