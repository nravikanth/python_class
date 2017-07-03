s=raw_input("Enter the string")
d={}
for i in s:
	if d.has_key(i):
		d[i]=d[i]+1
	else:
		d[i]=1
print d
