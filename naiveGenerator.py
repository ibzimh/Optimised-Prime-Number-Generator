import Main as main
import numpy as np
import makeListOfPrimes as lst
import random
import helperFunctions as arr
import primeHelpers as r


def nprime(n):
  q = r.rand_odd(n)
  t = 0
  while(not r.is_prime(q)):
    q = r.rand_odd(n)
    t += 1
  print("nprime trails: ", t)
  return q

def nprime2(n):
  q = r.is_prime(n)
  t = 0
  while(not r.is_prime(q) or t > 100):
    q += 2
    t += 1
  print("nprime2 trails: ", t)
  return q
