lista = input('dame una lista por separado de numeros').split( )
lista=list(map(int,lista))

mi = 0
me = mi
for i in lista:
	if i > mi:
		mi = i
	if i < me:
		me = i
print(mi)
print(me)

