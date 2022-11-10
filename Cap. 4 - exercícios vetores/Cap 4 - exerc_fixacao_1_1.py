#exercício vetores 
#Considerar que no livro a enumeração de índice da lista começa no 1 
#Porém em python começa no 0. Por isso, houveram adaptações.

vetor = [2,6,8,3,10,9,1,21,33,14]
x = 2
y = 4

a = vetor[x]
print(a)

b = vetor[x+1]
print(b)

c = vetor[x+2]
print(c)

d = vetor[x*4-1]
print(d)

e = vetor[x*1-1]
print(e)

f = vetor[x*2-1]
print(f)

g = vetor[x*3-1]
print(g)

h = vetor[vetor[x+y-1]-1]
print(h)

i = vetor[x+y-1]
print(i)

j = vetor[8-vetor[2-1]-1]
print(j)

l = vetor[vetor[4-1]-1]
print(l)

m = vetor[vetor[vetor[7-1]-1]-1]
print(m)

n = vetor[vetor[0]*vetor[3]-1]
print(n)

o = vetor[x+4-1]
print(o)