def main():
    pattern = ''
    while(True):
        try:
            pattern = input()
            if(pattern != "NAO QUERO MAIS" and len(pattern) <= 80):
                b = Spaces(pattern)
                a = Aas(pattern)
                print(b)
                print(a)
                Pairs(pattern)
            else:
                break
        except(EOFError):
            break
    
    
def Spaces(pattern): #Conta a qntd de espacos no pattern
    Spaces = 0
    first_letter = False
    for blankSpace in pattern: #Verifica se ? encontrada a primeira letra, se for encontrada come?a a contar
        if(blankSpace.isalpha() and first_letter == False):
            first_letter = True
        if(blankSpace == " " and first_letter == True):
            Spaces += 1
        elif(blankSpace == " " and first_letter == False):
            Spaces += 1
    return Spaces
    
def Aas(pattern): #Conta a qntd de "A" no pattern
    numAa = 0
    for Aa in pattern:
        if(Aa == "A"):
            numAa += 1
        elif(Aa == "a"):
            numAa += 1
    return numAa
    
def Pairs(pattern):
    aux = 0
    counting = ''
    best = 0
    frequency = []
    old_letters = ''
    pairs_list = []
    pattern = pattern.lower() #AB e suas combinacoes sao considerado os mesmos pares AB = ab
    for i in range(0,len(pattern)-1):#Verifica se ? uma letra e concatena com a pr?xima e adiciona na pairs_list
        if(pattern[i].isalpha() and pattern[i+1].isalpha()):
                pairs_list.append(pattern[i] + pattern[i+1])
    if(len(pairs_list) != 0):
        set_list = set(pairs_list) #Retira os elementos repetidos
        frequency = pairs_list.copy() 
        for pairs_search in set_list: #Procura na set_list(os nao repetidos) e remove da lista frequency, restando apenas os repetidos
            if(len(frequency) != 1):
                frequency.remove(pairs_search)
        for counting in frequency: #Conta na lista frequency quantas vezes cada elemento se repete.
            times = pairs_list.count(counting)
            if(times > aux): #Armazena o maior valor de repeticoes na variavel best
                aux = times
                best = aux
                best_counting = counting #Armazena o elemento de maior repeticao na variavel best_counting
            else:
                best = aux
    if(best > 1):
        print(best)
        print(best_counting)
    elif(best == 1):
        print(best)
        print(pairs_list[0])
    else:
        print("NENHUM PAR")
        

        
        
if __name__ == "__main__":
    main()
