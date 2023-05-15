
def minDistance(distancia, shortestPathSet,vertices):
  
        # Initialize minimum distanciaance for next node
        min = 10010
  
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(vertices):
            if distancia[u] < min and shortestPathSet[u] == False:
                min = distancia[u]
                min_index = u
  
        return min_index
  
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation

def dijkstra(grafo,vertices,comeco):
  
    distancia = [10010] * vertices
    distancia[comeco] = 0
    shortestPathSet = [False] * vertices
  
    for cout in range(vertices):
  
        # Pick the minimum distanciaance vertex from
        # the set of vertices not yet processed.
        # x is always equal to src in first iteration
        x = minDistance(distancia, shortestPathSet,vertices)
  
        # Put the minimum distanciaance vertex in the
        # shortest path tree
        shortestPathSet[x] = True
  
        # Update distancia value of the adjacent vertices
        # of the picked vertex only if the current
        # distanciaance is greater than new distanciaance and
        # the vertex in not in the shortest path tree
        for y in range(vertices):
            if grafo[x][y] > 0 and shortestPathSet[y] == False and \
                    distancia[y] > distancia[x] + grafo[x][y]:
                distancia[y] = distancia[x] + grafo[x][y]


def main():

    cidadeRemetente = cidadeDestinataria = precoPedagio = 0

    numCidades,numEstradas = map(int,input().split())
    grafo = []

    for i in range(numEstradas):
        cidadeRemetente,cidadeDestinataria,precoPedagio = map(int, input().split())

    dijkstra(grafo,numEstradas,1)


main()