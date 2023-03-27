buffer_1 = input().strip()
buffer_2 = input().strip()

hex_1 = int(buffer_1, 16)
hex_2 = int(buffer_2, 16)
xor = hex_1 ^ hex_2

print(hex(xor)[2:])
