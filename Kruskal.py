# Carlos Alejandro Mercado Villalvazo
from functools import cmp_to_key # librería para ordenar con comparadores

def comparator(a,b):
    return a[2] - b[2];

def kruskals_mst(V, edges):

    # Organizar las aristas por peso
    edges = sorted(edges,key=cmp_to_key(comparator))
    print("Aristas ordenadas por peso:", edges)
    # Moverse por las aristas en orden ascendente
    dsu = DSU(V)
    print("Conjuntos disjuntos iniciales:", dsu.parent)
    print("Rangos iniciales:", dsu.rank)
    cost = 0
    count = 0
    for x, y, w in edges:
        
        # Asegurarse de que no se forme un ciclo
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            print(f"Unir {x} y {y} con peso {w}")
            print("Conjuntos disjuntos actualizados:", dsu.parent)
            print("Rangos actualizados:", dsu.rank)
            cost += w
            count += 1
            if count == V - 1:
                break
    print("Costo total del MST:", cost)
    print("Conjuntos disjuntos finales:", dsu.parent)
    print("Rangos finales:", dsu.rank)
    return cost
    
# Clase para el manejo de conjuntos disjuntos (DSU)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    # Método para encontrar el representante del conjunto al que pertenece un elemento
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Método para unir dos conjuntos
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


if __name__ == '__main__':
    
    # Una arista contiene peso, origen y destino
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print("El peso final de unir los vértices es:",kruskals_mst(4, edges))
