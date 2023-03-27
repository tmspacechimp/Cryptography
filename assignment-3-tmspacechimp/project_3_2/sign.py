from oracle import *
from helper import *
from math import sqrt

def get_signature(m, n):
  for i in range(2, int(sqrt(m))):
    if m % i == 0:
      signature = (pow(Sign(1), -1, n) * Sign(i) * Sign(m // i)) % n
      return signature


def main():
  with open('project_3_2/input.txt', 'r') as f:
    n = int(f.readline().strip())
    msg = f.readline().strip()

  Oracle_Connect()

  m = ascii_to_int(msg)
  sigma = get_signature(m, n)

  print(sigma)

  Oracle_Disconnect()

if __name__ == '__main__':
  main()
