def sum (list,L=[]):
	if len(L)==0:
		L.append(0)
	if len(list) !=0:
		L[0]+=list[0]
		list.remove(list[0])
		return sum(list)
	return L[0]


list = [1,2,3,4]
s=sum(list)
print(s)
	
