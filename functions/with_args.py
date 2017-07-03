import pudb
def fun1(a,b=30,c=40):
	s=a+b+c
	return s

a=10
b=20
pudb.set_trace()
c=fun1(a,b)
print c