import sys

from oracle import Mac, Oracle_Connect, Oracle_Disconnect


def read_from_file():
    name = sys.argv[1]
    with open(name) as file:
        return file.read().strip()

def xor(tag, block):
    xor = ''
    for i in range(min(len(tag), len(block))):
        xor += chr(tag[i] ^ block[i])
    return xor


def forge(message):
    # we can get a tag for 32 byte long strings,
    # how you would forge this is taking two 16 byte blocks:
    # b1 ^ t and b2. for a longer string we would just repeat
    # this for 32 byte block pairs.

    tag = bytearray([0] * 16)
    for i in range(0, len(message), 32):
        b1 = message[i: i + 16]
        b2 = message[i + 16: i + 32]
        new_pair = xor(tag, bytearray(b1, 'utf-8')) + b2

        tag = Mac(new_pair, len(new_pair))

    return tag



if __name__ == '__main__':
    Oracle_Connect()
    print(forge(read_from_file()).hex())
    Oracle_Disconnect()






