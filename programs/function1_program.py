import pudb
def sum_of(a,b):
	c =  a+b
	return c

if  __name__== '__main__':
	a = input('enter a value')
	b= input('enter b value')
	pudb.set_trace()
	c = sum_of(a,b)
	print c

