def fact(a):
	
	if a==0:
		return 0
	else:
		a * fact(a-1)

x=int(input("ingrese numero para fatorial"))
fact(x)
