def fun(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (fun(n-1)+fun(n-2))
inp=int(input("Введите число "))

print(fun(inp))
