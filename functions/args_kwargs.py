import pudb
def fun1(a,*args, **kwargs):
	print args
	print kwargs
	return None

a=10
b=20
pudb.set_trace()
c=fun1(a,b, c=10, b=20)
print c