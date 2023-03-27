import base64

frequencies = {'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
               'e': 0.1041442, 'f': 0.0197881,
               'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
               'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124,
               'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606,
               'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
               'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
               'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182}


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return 0
    b1 = bytearray(s1, 'utf-8')
    b2 = bytearray(s2, 'utf-8')

    distance = sum(bin(b1[i] ^ b2[i]).count("1") for i in
                   range(max(len(b1), len(b2))))
    return distance


def find_key_size(text):
    min_distance = float('inf')
    for k in range(2, 41):
        distances = 0
        normalizer = 0
        for i in range(len(text) - 2 * k + 1):
            distances += hamming_distance(text[i: i + k],
                                          text[i + k: i + 2 * k]) / k
            normalizer += 1
            i += k
        normalized_distance = distances / normalizer
        if normalized_distance < min_distance:
            min_distance = normalized_distance
            key_size = k

    return key_size


def find_single_byte_key(text):
    bytes = bytearray(text, 'utf')
    best_key = 0
    best_score = 0.0
    for i in range(256):
        score = 0.0
        decryption = bytearray([b ^ i for b in bytes])
        for byte in decryption:
            char = chr(byte)
            if char in frequencies:
                score += frequencies[char]
        if score > best_score:
            best_score = score
            best_key = i
    return chr(best_key)


def encrypt_with_repeating_key(text, key):
    text_bytes = bytearray(text, 'utf-8')
    key_bytes = bytearray(key, 'utf-8')
    xor = bytearray()
    for i in range(len(text_bytes)):
        xor.append(text_bytes[i] ^ key_bytes[i % len(key_bytes)])

    return xor.decode()


message = base64.b64decode(input().strip()).decode()
key_size = find_key_size(message)

kth_letters = [''] * key_size
for i in range(len(message)):
    kth_letters[i % key_size] += message[i]

key = ''
for s in kth_letters:
    key += find_single_byte_key(s)

print(encrypt_with_repeating_key(message, key))
