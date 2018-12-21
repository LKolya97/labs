lst=[]
n=5
lst1=[]
max=-1
n=int(input("Введите количество остановок: "))
for l in range(1, n+1):
    lst.append(0)
S=input("Введите данные пассажира: ")
while S!="":
     a=S.find(" ")
     S=S[a+1:len(S):1]
     a=S.find(" ")
     S=S[a+1:len(S):1]
     a=S.find(" ")
     i=int(S[0:a:1])
     j=int(S[a+1:len(S):1])
     while i<j:
        lst[i-1]+=1
        i+=1
     S=input("Введите данные пассажира или нажмите Enter: ")
for l in range(1, n+1):
 
 if lst[l-1]>max:
     max=lst[l-1]
     lst1=[]
     lst1.append(l-1)
 elif lst[l-1]==max:
     lst1.append(l-1)
for l in range(0,len(lst1)):
    print(str(lst1[l]+1)+"-"+str(lst1[l]+2))
     
