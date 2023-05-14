
#verifica pra quem o i esta apontando(encontra a "arvore" de i)
#para ver qual a raiz da arvore onde o nó se encontra
def find(pai, i):
        
        if pai[i] != i:
            pai[i] = find(pai, pai[i])
        return pai[i]

def union(pai, rank, x, y):
 
        #coloca a arvore de menor ranque embiaxo da de maior ranque
        if rank[x] < rank[y]:
            pai[x] = y
        elif rank[x] > rank[y]:
            pai[y] = x
 
        #se ranks forem o mesmo coloca um(arbitrario) como pai do outro
        #e incrementa o rank do pai
        else:
            pai[y] = x
            rank[x] += 1

def Kruskal(vertices,grafo,soma): 
        result = []
        i = 0
        e = 0
        minimumCost = 0

        grafo = sorted(grafo,key=lambda item: item[2])
 
        pai = []
        rank = []
 
        for node in range(vertices):
            pai.append(node)
            rank.append(0)
 
        while e < vertices - 1:

            u, v, w = grafo[i]
            i = i + 1
            x = find(pai, u)
            y = find(pai, v)
 
            # se incluir essa aresta (grafo[i]) nao causar ciclos, então
            # coloque-a no resultado(MST) e adiciona 1 pro contador de vertices
            if x != y:
                e = e + 1
                result.append([u, v, w])
                union(pai,rank,x,y)
                
            # Caso contrario descarta a aresta e pula pra proxima do grafo
            # sem incrementar o contador de vertices.
 
        
        for u, v, w in result:
            minimumCost += w
        print(soma - minimumCost)


def main():

  soma = 0
  grafo = []

  while(1):
    juncoes,estradas = map(int,input().split())
    grafo = []
    soma = 0
    if(juncoes == 0 and estradas == 0):
        break

    for i in range(estradas):
        nodeX,nodeY,metros = map(int, input().split())
        #soma total de todos os pesos para ser subtraida da arvore minima após, e encontrar a economia de byteland
        soma += metros
        grafo.append([nodeX,nodeY,metros])
    Kruskal(juncoes,grafo,soma)



main()
