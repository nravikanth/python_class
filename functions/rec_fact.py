import pudb
def rec(n):
	if n<=1:
		return 1
	return n* rec(n-1)

a=5
pudb.set_trace()
print rec(a)