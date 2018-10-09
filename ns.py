def fact(a):
	
	if a==0:
		return 0
	else:
		fact(a-1)*fact(a)

x=int(input("ingrese numero para fatorial"))
fact(x)
