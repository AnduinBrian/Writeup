# (bt[0] ^ 16) != 74
# (bt[1] ^ 17) != 87
# (bt[2] ^ 33) != 77
# (bt[3] ^ 51) != 70
# (bt[4] ^ 68) != 29
# (bt[5] ^ 102) != 49
# (bt[6] ^ 51) != 117
# (bt[7] ^ 160) != 238
# (bt[8] ^ 144) != 241
# (bt[9] ^ 181) != 226
# (bt[10] ^ 238) != 163
# (bt[11] ^ 17) != 44

import base64
flag = ""

for i in range(12):
	for j in range(32,128):
		if i == 0:
			if 16^74 == j:
				flag += chr(j)
				break
		if i == 1:
			if 17^87 == j:
				flag += chr(j)
				break
		if i == 2:
			if 33^77 == j:
				flag += chr(j)
				break
		if i == 3:
			if 51^70 == j:
				flag += chr(j)
				break
		if i == 4:
			if 68^29 == j:
				flag += chr(j)
				break
		if i == 5:
			if 102^49 == j:
				flag += chr(j)
				break
		if i == 6:
			if 117^51 == j:
				flag += chr(j)
				break
		if i == 7:
			if 160^238 == j:
				flag += chr(j)
				break
		if i == 8:
			if 144^241 == j:
				flag += chr(j)
				break
		if i == 9:
			if 181^226 == j:
				flag += chr(j)
				break
		if i == 10:
			if 238^163 == j:
				flag += chr(j)
				break
		if i == 11:
			if 17^44 == j:
				flag += chr(j)
				break

print "Found pass: " + base64.b64decode(flag)







