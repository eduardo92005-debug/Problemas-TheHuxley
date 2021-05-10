string = input().split()
L = int(string[0])
U = int(string[1])
primos = []
diferenca = []
numbers_in_range = [i for i in range(1,U+1)]
contador = 0
larger = 1
larger_dic = {}
if(0 < L and L < 1000):
    for i in numbers_in_range:
        for k in range(1,U+1):
            if(i % k == 0):
                contador += 1
        if(contador == 2):
            primos.append(i)
            contador = 0
        contador = 0
    for i in range(0,len(primos)):
        for k in range(0,len(primos)):
            try:
                if(primos[i] < L):
                    primos.pop(i)
            except IndexError:
                break
    for i in range(0,len(primos)-1):
        diference = primos[i+1] - primos[i]
        diferenca.append(diference)
    for numbers in diferenca:
        larger_dic[numbers] = larger_dic.get(numbers,0)+1
    try:
        larger = max(larger_dic.values())
        equal = 0
        for i in larger_dic.values():
            if(larger == i):
                equal += 1
        if(equal == 2):
            print("-1\n")
        else:
            print("%d\n"%list(larger_dic.keys())[list(larger_dic.values()).index(larger)])
    except ValueError:
        print("-1\n")
