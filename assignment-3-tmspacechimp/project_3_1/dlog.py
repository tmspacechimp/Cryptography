from math import sqrt, ceil


def get_map(p, g, h, b):
	left = pow(g, -1, p)
	map = {}
	for i in range(b):
		map[h] = i
		h = pow((h * left), 1, p)
	return map


def find_in_map(p, g, b, map):
	right = pow(g, b, p)
	value = 1
	for i in range(b):
		if value in map:
			return i * b + map[value]
		value = pow((value * right), 1, p)


# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(p, g, h, max_x):
	b = int(ceil(sqrt(max_x)))
	map = get_map(p, g, h, b)
	return find_in_map(p, g, b, map)


def main():
	p = int(input().strip())
	g = int(input().strip())
	h = int(input().strip())
	max_x = 1 << 40  # 2^40

	dlog = discrete_log(p, g, h, max_x)
	print(dlog)


if __name__ == '__main__':
	main()
