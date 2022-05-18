import random
n=4 # numero de ciudades
m=5 # numero de items
vmax = 1 # velocidad maxima
vmin = 0.1 # velocidad minima
W=3 # peso maximo
Wk = [3,1,1,2,3]
pk = [100,40,40,20,30]
d = [[-1,5,6,6],[5,-1,5,6],[6,5,-1,4],[6,6,4,-1]]


#modulo de inicializacion
x=[1,2,4,3]
z=[0,3,3,0,0]


#funcion f
ciudadesutilizadas = []
for item in z:
    if item != 0:
        if item not in ciudadesutilizadas:
            ciudadesutilizadas.append(item)
fxz = 0
vc=1
wc=0
for i in x:
    for j in x:
        if x.index(i) - x.index(j) == -1:
            if i in ciudadesutilizadas:
                for item in z:
                    if item == i:
                        wc+=Wk[z.index(item)]
                vc = vmax - wc*(vmax-vmin)/W
                fxz += d[i-1][j-1]/vc
            else:
                fxz += d[i-1][j-1]/vc
        if x.index(i) == n-1 and x.index(j)==0:
            if i in ciudadesutilizadas:
                for item in z:
                    if item == i:
                        wc+=Wk[z.index(item)]
                vc = vmax - wc*(vmax-vmin)/W
                fxz += d[i-1][j-1]/vc
            else:
                fxz += d[i-1][j-1]/vc

print("El valor de f(xz) es: ",fxz)

#funcion g
itemsutilizados = []
for i in range(m):  # ciclo para obtener los items utilizados
    if z[i] != 0:
        itemsutilizados.append(i)
gz= 0
for i in itemsutilizados:
    gz+=pk[i]
print("El valor de g(z) es: ",gz)

# funcion G(xz)
Gxz = gz-fxz
print("El valor de G(xz) es: ",Gxz)

# modulo de destruccion
# d_viajero es el numero de ciudades destruidas.
# d_item es el numero de items destruidos.
d_viajero = 1
d_item = 1
# se remueve una ciudad aleatoria
dviajero = random.randint(0,n-1) 
del x[dviajero]
ditem = random.randint(0,m-1)
del z[ditem]
print("ciudad eliminada: ",dviajero+1)
print("item eliminado: ",ditem+1)
print(x,z)

#modulo de construccion

