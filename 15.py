    
def printm(A,n):
    i=0
    while i<n:
        j=0
        while j<n:
            print(A[i][j], end=" ")
            j+=1
        i+=1
        print()
        
def copym(A,B,n):
    i=0
    while i<n:
        j=0
        B.append([])
        while j<n:
            B[i].append(A[i][j])
            j+=1
        i+=1
        
def minor(A,i,j,n):
    M = []
    copym(A,M,n)
    del M[i]
    for i in range(len(A[0])-1):
        del M[i][j]
    return M   
    
def det(A):
    m = len(A)
    n=len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    sig = 1
    deter = 0
    for j in range( n ):
        deter += A[0][j]*sig*det(minor(A,0,j,n)) 
        sig *= -1
    return deter                           
      
  
mass=[]
i=0
n=int(input("Введите размерность матрицы "))
while i<n:
    mass.append([])
    j=0
    while j<n:
        num=int(input("Введите число "))
        mass[i].append(num)
        j+=1
    i+=1    
printm(mass,n)    
print("определитель матрицы = "+str(det(mass)))

