#This function results the addition of the arguments passed
import pudb
def check_result(fun):
	def wrapper(*args, **kwargs):
		a=fun(*args, **kwargs)
		if a%2==0:
			return "Even"
		else:
			return "Odd"
	return wrapper


@check_result
def sum_fun(a):
	c=sum(a)
	return c


a=[1,2,3,4,5,7]
pudb.set_trace()
res=sum_fun(a)
print res
