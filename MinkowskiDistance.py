class Distance:
    """ This class provides methods to calculate the Minkowski's family"""
    def manhattan(self, x, y):
        d=0.0
        for k in range(len(x)):
            d += abs((x[k]-y[k]))
        return d
    def euclidean(self, x, y):        
        d = 0.0
        for k in range(len(x)):
            d += abs((x[k]-y[k]))**2
        return d**(1.0/2.0)
    def minkowski(self, x, y, p):
        d = 0.0
        for k in range(len(x)):
            d+= abs((x[k]-y[k]))**p
        return d**(1.0/p)

# Exemplo
a = (1, 2, 3)
b = (4, 5, 6)
dist = Distance()
print(dist.minkowski(a,b,1))
print(dist.minkowski(a,b,2))
print("")
print(dist.manhattan(a,b))
print(dist.euclidean(a,b))
