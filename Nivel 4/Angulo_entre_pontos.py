import math
    
def dotProd_Angle(vectorA,vectorB): #Calculo do angulo entre dois vetores pelo produto interno
    alpha = 0
    prod_vector = 0
    for i in range(0,2):
        prod_vector += vectorA[i]*vectorB[i]
    alpha = prod_vector/math.sqrt(modVector(vectorA)*modVector(vectorB))
    return math.degrees(math.acos(alpha))
#Inicializacao    
a = input()
b = input()
c = input()
a = a.split()
b = b.split()
c = c.split()
v = [] #AB
u = [] #AC
w = [] #BC
modVector = lambda vector:(vector[0]**2) + (vector[1]**2) #Norma do vetor
for i in range(0,2): #Preenchendo valores para os vetores
    a.insert(i,int(a.pop(i)))
    b.insert(i,int(b.pop(i)))
    c.insert(i,int(c.pop(i)))
    v.append(b[i] - a[i]) #AB = v -> AB = B - A, AC = u -> C - A, BC = w -> C - A
    u.append(c[i] - a[i]) 
    w.append(c[i] - b[i])
#Como os pontos nuncam sao colineares, entao, isso quer dizer que sempre sera formado um triangul
angulo_vu = dotProd_Angle(v,u)
angulo_wu = dotProd_Angle(w,u)
anguloabc = abs((angulo_vu + angulo_wu) - 180) #Assim, achando-se dois angulos, podemos achar o terceiro diminuindo 180
print("%.2f"%anguloabc)

    
