lista = input('dame una lista por separado de numeros').split( )
lista=list(map(int,lista))

mi = 0
for i in lista:
	if i > mi:
		mi = i
print(mi)