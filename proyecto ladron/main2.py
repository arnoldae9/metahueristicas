import random
import numpy as np
import copy
import itertools
from itertools import combinations
for alfa in [0.1,0.01,0.001,0.0001,0.00001,0.000001]:
    inf = np.inf
    def convertiraenteros(lista):
        for indice,valor in enumerate(lista):
            lista[indice] = int(valor)
        return lista
    def distancia(a, b):
        return ((a[1]-b[1])**(2)+(a[2]-b[2])**(2))**0.5
    with open('4461.txt','r') as archivo:
        datos = archivo.read().split("\n")
        nombre = datos[0].split()[2]
        tipo = datos[1].split()[3]+datos[1].split()[4]+datos[1].split()[5]
        n = int(datos[2].split()[1])
        m = int(datos[3].split()[3])
        W = int(datos[4].split()[3])
        vmax = float(datos[5].split()[2])
        vmin = float(datos[6].split()[2])
        R = float(datos[7].split()[2])
        nodos = []
        d=[]
        pk=[]
        Wk = []
        disponibilidad = []
        i = 0
        for i in range(4461): #TODO nodo (x,y)
            linea = datos[i+10].split()
            linea = convertiraenteros(linea)
            nodos.append(linea)
        print(len(nodos))
        for i in range(len(nodos)): #TODO valor de la matriz d
            renglon=[]
            for j in range(len(nodos)):
                renglon.append(distancia(nodos[i],nodos[j]))
            d.append(renglon)
        print(len(d))
        for i in range(4460): #TODO pk valores
            pki = datos[i+4472].split()[1]
            pk.append(pki)
            Wki = datos[i+4472].split()[2]
            Wk.append(Wki)
            disponibilidadi = datos[i+4472].split()[3]
            disponibilidad.append(disponibilidadi)
        pk = convertiraenteros(pk)
        Wk = convertiraenteros(Wk)
        disponibilidad = convertiraenteros(disponibilidad)
        pk = convertiraenteros(pk)
        Wk = convertiraenteros(Wk)
    #disponibilidad = [[inf],[4,5],[1,2,3],[4]]
    #TODO  modulo de inicializacion
    x=[]
    wc = 0
    z = []
    for i in range(m):
        z.append(0)
    vc=1
    gz=0
    def solinicial(x,d):
        nodoinicial = 1
        x.append(nodoinicial)
        posibles = []
        while len(x) < n:
            minimo = inf    
            for indice, valor in enumerate(d[nodoinicial-1]):
                if indice + 1 not in x:
                    if valor < minimo:
                        minimo = copy.deepcopy(valor)
            for indice, valor in enumerate(d[nodoinicial-1]):
                if valor == minimo:
                    posibles.append(indice)
            nodosiguiente = random.choice(posibles) + 1
            if nodosiguiente not in x:
                x.append(nodosiguiente)
                nodoinicial = copy.deepcopy(nodosiguiente)
        return x

    #TODO  funcion f
    def f(z,x,Wk,vmin,vmax,W,vc,wc,d):
        wc=0
        ciudadesutilizadas = []
        for item in z:
            if item != 0:
                if item not in ciudadesutilizadas:
                    ciudadesutilizadas.append(item)
        fxz = 0
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



    #TODO  funcion gz
    def g(m,gz,pk,z):
        itemsutilizados = []
        for i in range(m):  # ciclo para obtener los items utilizados
            if z[i] != 0:
                itemsutilizados.append(i)
        for i in itemsutilizados:
            gz+=pk[i]
        return gz


    #TODO funcion Gxz
    def Gxz(gz,fxz,R):
        return gz-R*fxz

    #TODO  modulo de destruccion
    # d_viajero es el numero de ciudades destruidas.
    # d_item es el numero de items destruidos.




    #TODO  se remueve una ciudad aleatoria
    def eliminarciu(x):
        ciuelim = [] # ciudades eliminadas
        d_viajero = random.randint(2,4460)
        for i in range(d_viajero):
            dviajero = random.randint(2,4461)
            while(dviajero not in x):
                dviajero = random.randint(2,4461)
            x.remove(dviajero)
            ciuelim.append(dviajero)
        return ciuelim

    #TODO  se remueve un item aleatorio
    def eliminaritem(z,wc):
        itemelim = [] # items eliminados
        d_item = random.randint(1,4460)
        for i in range(d_item):
            ditem = random.randint(1,4460)
            while(ditem in itemelim):
                ditem = random.randint(1,4460)
            itemelim.append(ditem)

            for index, value in enumerate(z):
                if value == ditem:
                    z[index] = 0
                    wc -= Wk[index]
        return wc,itemelim

    #TODO  modulo de contrucci??n ciudades
    def consciu(ciuelim,x,d):
        while bool(ciuelim) == True:
            ultimaciudad = x[-1]
            #print(ultimaciudad)
            distanciamenor = inf
            for item in ciuelim:
                if d[ultimaciudad-1][item-1] < distanciamenor:
                    distanciamenor = copy.deepcopy(d[ultimaciudad-1][item-1])
                    nodoappend = item
                    #print(nodoappend)
            x.append(nodoappend)
            ciuelim.remove(nodoappend)
            #print("ciuelim",ciuelim)
            #print("x",x)
        return x

    def busqueda(x):
      for indice, valor in enumerate(x):
        if indice > 0 and indice < len(x)-1:
            y = copy.deepcopy(x)
            y[indice] = copy.deepcopy(x[indice + 1 ])
            y[indice + 1 ] = copy.deepcopy(x[indice])
            f1 = f(z,x,Wk,vmin,vmax,W,vc,wc,d)
            f2 = f(z,y,Wk,vmin,vmax,W,vc,wc,d)
            print(f1,f2)
            if f2 < f1:
                x = copy.deepcopy(y)
                break
      return x

    def consciu2(x,ciuelim,d,alfa): #TODO consciu2
      while len(x) < n:
        listcostdisp = []
        ciudadesdisp = []
        nodoi = x[-1]
        for ciudad,i in enumerate(ciuelim):# costosdisponibles = costdisp
          costdisp = d[nodoi-1][i-1]
          listcostdisp.append(costdisp)
        if len(listcostdisp) >= 2: 
          max = np.max(listcostdisp)
          min = np.min(listcostdisp)
          rango = max - min
          cijmin = min+rango*alfa
          seleccionables = []
          for indice, valor in enumerate(d[nodoi-1]):
            if valor <= cijmin:
              if indice + 1 not in seleccionables and indice +1 not in x:
                seleccionables.append(indice+1)
          nodosiguiente = random.choice(seleccionables)
          x.append(nodosiguiente)
          ciuelim.remove(nodosiguiente)
        else:
          for item in range(1,n+1):
            if item not in x:
              x.append(item)
      return x

    def empty(seq): 
        try: 
            return all(map(empty, seq)) 
        except TypeError: 
            return False 

    #TODO construcci??n de items
    #TODO disponibilidad = [[3],[3],[3],[2,4],[2]] #item[ciudad]
    #TODO z=[0,3,3,0,0] item[ciudad]
    def construcci??nitems(disponibilidad,wc,W,z,Wk):
        dispoaux = copy.deepcopy(disponibilidad)
        while empty(dispoaux) == False:
            if wc == W:
                break
            for indice,valor in enumerate(z):
                try:
                    if valor != 0:
                        dispoaux[indice].remove(valor)
                except:
                    continue
            #inicialiacion de ciudad
            itemrandom = random.randint(1,m)
            while  len(dispoaux[itemrandom-1]) == 0: # ciclo para evitar la ciudad 1
                itemrandom = random.randint(1,m) # ciudad es la ciudad random seleccionada
            prueba =  wc + Wk[itemrandom-1]
            ciudad = random.choice(dispoaux[itemrandom-1])
            if prueba <= W and empty(dispoaux[itemrandom-1]) == False:
                z[itemrandom-1]=ciudad #asignaci??n en el vector z
                wc += Wk[itemrandom-1] #actualizaci??n de wc
            dispoaux[itemrandom-1].remove(ciudad)
        return z,wc

    #TODO main
    contador =0
    xinicial = solinicial(x,d)
    zinicial, wcinicial = construcci??nitems(disponibilidad,wc,W,z,Wk)
    while contador < 1:
        finicial = f(zinicial,xinicial,Wk,vmin,vmax,W,vc,wcinicial,d)
        gzinicial = g(m,gz,pk,zinicial)
        Gxzinicial =  Gxz(gzinicial,finicial,R)
        ciuelim = eliminarciu(xinicial)
        wc2, itemelim = eliminaritem(zinicial,wcinicial)
        x2=consciu2(xinicial,ciuelim,d,alfa)
        #x2 = busqueda(x2)
        #x2=consciu(ciuelim,xinicial,d)
        z2,wc2=construcci??nitems(disponibilidad,wc2,W,zinicial,Wk)
        ffinal = f(z2,x2,Wk,vmin,vmax,W,vc,wc2,d)
        gzfinal = g(m,gz,pk,z2)
        Gxzfinal = Gxz(gzfinal,ffinal,R)
        # if Gxzfinal >= Gxzinicial:
        if ffinal <= finicial or gzfinal >= gzinicial:
        # if ffinal <= finicial and gzfinal >= gzinicial:
            contador+=1
            zinicial=z2
            xinicial=x2
            wcinicial=wc2
            print(contador)
    print(zinicial,xinicial,Gxzinicial)

    with open('resultados.txt','a') as resultados:
        texto = "\n"+"alfa: " + str(alfa) + " Gxz: " + str(Gxzinicial)  
        resultados.write(texto)    

#FIXME probablemente si la construcci??n no es por vecinos mas cercanos no me quede en 45