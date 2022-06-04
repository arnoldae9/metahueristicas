import random
n=4 # numero de ciudades
m=5 # numero de items
vmax = 1 # velocidad maxima
vmin = 0.1 # velocidad minima
W=3 # peso maximo
Wk = [3,1,1,2,3]
pk = [100,40,40,20,30]
d = [[-1,5,6,6],[5,-1,5,6],[6,5,-1,4],[6,6,4,-1]]
fxz = 0
vc=1
wc=0
#modulo de inicializacion
x=[1,2,4,3]
z=[0,3,3,0,0]
fxz = 0
vc=1
wc=0
gz= 0
#funcion f
def f(z,x,Wk,vmin,vmax,W,fxz,vc,wc):
    ciudadesutilizadas = []
    for item in z:
        if item != 0:
            if item not in ciudadesutilizadas:
                ciudadesutilizadas.append(item)
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
    return fxz
fxz = f(z,x,Wk,vmin,vmax,W,fxz,vc,wc)
print("El valor de f(xz) es: ",fxz)


#funcion g
def g(m,gz,pk):
    itemsutilizados = []
    for i in range(m):  # ciclo para obtener los items utilizados
        if z[i] != 0:
            itemsutilizados.append(i)
    for i in itemsutilizados:
        gz+=pk[i]
    return gz

gz = g(m,gz,pk)
print("El valor de g(z) es: ",gz)

# funcion G(xz)
def Gxz(gz,fxz):
    return gz-fxz
Gxz = Gxz(gz,fxz)
print("El valor de G(xz) es: ",Gxz)

# modulo de destruccion
# d_viajero es el numero de ciudades destruidas.
# d_item es el numero de items destruidos.
# se remueve una ciudad aleatoria
def eliminarciu(x):
    ciuelim = [] # ciudades eliminadas
    d_viajero = random.randint(1,3)
    for i in range(d_viajero):
        dviajero = random.randint(1,4)
        while(dviajero not in x):
            dviajero = random.randint(1,4)
        x.remove(dviajero)
        ciuelim.append(dviajero)
    return ciuelim
    
ciuelim = eliminarciu(x)

# se remueve un item aleatorio
def eliminaritem(z):
    itemelim = [] # items eliminados
    d_item = random.randint(1,5)
    for i in range(d_item):
        ditem = random.randint(1,5)
        while(ditem in itemelim):
            ditem = random.randint(1,5)
        itemelim.append(ditem)
    
        for index, value in enumerate(z):
            if value == ditem:
                z[index] = 0
    return itemelim

itemelim = eliminaritem(z)

print(z)
print(x)
print(ciuelim)
print(itemelim)
