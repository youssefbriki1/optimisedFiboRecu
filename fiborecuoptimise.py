calculated = set()
dico = {0:1,1:1}

    
def fibo(n):
    global calculated, dico
    if n <= 1:
        return 1
    else:
        if n in calculated:
            return dico[n]
        else:
            calcul = fibo(n-1)+fibo(n-2)
            dico[n] = calcul
            return calcul

print(fibo(16))
print(dico)
print(fibo(3))