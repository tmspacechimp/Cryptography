key = bytearray(input().strip(), 'utf-8')
text = bytearray(input().strip(), 'utf-8')

xor = bytearray()
for i in range(len(text)):
    xor.append(text[i] ^ key[i % len(key)])

print(xor.hex())
