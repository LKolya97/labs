S=input("Введите строчные латинские буквы ")
i=0
j=len(S)-1
start=0
while i!=j:
    if S[i]==S[j]:
        i+=1
        j-=1
    else:
        start+=1
        j=len(S)-1
        i=start 
print(start)    
