xor_string = [0x43,0x6B,0x66,0x6B,0x62,0x75,0x6C,0x69,0x4C,0x45,0x5C,0x45,0x5F,0x5A,0x46,0x1C,0x07,0x25,0x25,0x29,0x70,0x17,0x34,0x39,0x01,0x16,0x49,0x4C,0x20,0x15,0x0B,0x0F,0xF7,0xEB,0xFA,0xE8,0xB0,0xFD,0xEB,0xBC,0xF4,0xCC,0xDA,0x9F,0xF5,0xF0,0xE8,0xCE,0xF0,0xA9]
key = []
count = 0
flag = ""

for s in range(0,50):
	key.append(s*4)

for a in key:
	count += 1
	print "{0}: {1}".format(count,hex(a))

for i in range(0,len(xor_string)):
	flag += chr(xor_string[i] ^ (i*4))
	
print flag







