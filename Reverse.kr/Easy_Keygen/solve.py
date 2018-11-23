import binascii

d = binascii.unhexlify("5B134977135E7D13")

s = [0x10,0x20,0x30]

input_name = ""

for i in range(0,len(d)):
	input_name += chr(ord(d[i])^s[i%3])
	# print input_name
print input_name
	