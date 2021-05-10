n = int(input())
regras = {}
#cria um dicionario com as regras
for x in range(n):
    entrada = input().split(" => ")
    regras[entrada[0]] = entrada[1]
while(True):
    frase = input()
    aux = ''
    if(frase != "*"):
        frase = frase.split()
        for chave,valor in regras.items():
            for k in range(len(frase)):
                if(chave == frase[k]):
                    frase[k] = frase[k].replace(chave,valor)
        print(*frase)
    else:
        break
