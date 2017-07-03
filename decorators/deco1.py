#This function results the addition of the arguments passed
import pudb
def check_args(fun):
	def wrapper(*args, **kwargs):
		for i in args:
			if isinstance(i,int):
				pass
			else:
				return None
		return fun(*args, **kwargs)
	return wrapper


@check_args
def add_fun(a,b):
	c=a+b
	return c


if "__main__"=="__name__":
	a=10
	b=20
	pudb.set_trace()
	res=add_fun(a,b)
	print res
