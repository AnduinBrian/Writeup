def confirm(name,serial):
	v1=ord(name[0])
	v2= (v1&1)+5
	v3= ((v1 >> 4) & 1) +5
	v4= ((v1 >> 1) & 1 )+5
   	v5= ((v1 >> 2) & 1) +5
   	v6 = ((v1 >> 3) & 1) + 5
   	v7 = ord(name[1])
   	v8 = (v7 & 1) + 1
   	v9 = ((v7 >> 4) & 1) + 1
   	v10 = ((v7 >> 1) & 1) + 1
	v11 = ((v7 >> 2) & 1) + 1
	v12 = ((v7 >> 3) & 1) + 1


   	if str(v2 + v11) == serial[0]:
		if str(v6 + v12) == serial[1]:
			if str(v4 + v9) ==serial[2]:
				if str(v5 + v8) == serial[3]:
					if str(v3 + v10) == serial[4]:
						print name

serial= "76876-77776"

for i in range(97,122):
	for j in range(97,122):
		name = chr(i)+chr(j)
		confirm(name,serial)

print "====================================="

for i in range(97,122):
	for j in range(97,122):
		name = chr(i)+chr(j)
		confirm(name,serial[6:])

