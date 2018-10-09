def fact(a):
	
	if a==0:
		return 1
	else:
		return a * fact(a-1)

x=int(input("ingrese numero para fatorial"))
print (fact(x))
