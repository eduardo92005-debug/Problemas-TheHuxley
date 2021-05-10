entrada = input().split()
numeros = []
aux_count = 0
moda = 0
for i in list(map(int,entrada)):
    numeros.append(i)
for i in numeros: 
    count = numeros.count(i)
    if(count > aux_count):
        moda = i
        aux_count = count
print("Moda =",moda)
    
