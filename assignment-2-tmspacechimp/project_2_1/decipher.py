from oracle import Oracle_Connect, Oracle_Disconnect, Oracle_Send
import sys


def read_file():
    name = sys.argv[1]
    with open(name) as file:
        text = file.read().strip()
    return text


def final_part(cypher, block_amount, ans):
    for i in range(2, 17):
        for j in range(1, i):
            cypher[-16 - j] ^= (i ^ (i - 1))
        x = -1
        for b in range(256):
            cypher[-16 - i] ^= b
            reponse = Oracle_Send(cypher, block_amount - i)
            cypher[-16 - i] ^= b
            if reponse == 1:
                x = b
                break
        cypher[-16 - i] ^= x
        ans.append(x ^ i)
    for i in range(1, 17):
        cypher[-16 - i] ^= (16 ^ ans[-17 + i])
    cypher = cypher[:-16]


if __name__ == '__main__':
    cypher = [(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)]
    num_blocks = int(len(cypher) / 16)
    Oracle_Connect()
    ans = []
    for i in range(num_blocks - 1):
        last_byte_1 = -1
        last_byte_2 = -1
        for j in range(256):
            cypher[-17] ^= j
            response = Oracle_Send(cypher, num_blocks - i)
            cypher[-17] ^= j
            if response == 1:
                if last_byte_1 == -1:
                    last_byte_1 = j
                    continue
                if last_byte_2 == -1:
                    last_byte_2 = j
                    break
        cypher[-17] ^= last_byte_1
        cypher[-18] ^= 1
        response = Oracle_Send(cypher, num_blocks - i)
        cypher[-17] ^= last_byte_1
        cypher[-18] ^= 1
        if response == 0:
            last_byte_1 = last_byte_2
        cypher[-17] ^= last_byte_1
        ans.append(last_byte_1 ^ 1)
        final_part(cypher, num_blocks, ans)
    found = False
    s = ''
    for i in range(ans[0], len(ans)):
        s = chr(ans[i]) + s
    print(s)
    Oracle_Disconnect()

