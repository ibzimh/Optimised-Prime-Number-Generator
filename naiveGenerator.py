import Main as main
import numpy as np
import makeListOfPrimes as lst
import random
import helperFunctions as arr
import primeHelpers as r


def nprime(n):
  q = r.rand_odd(n)
  while(not r.is_prime(q)):
    q = r.rand_odd(n)
  return q

# slightly more efficent 
def nprime2(n):
  q = r.is_prime(n)
  while(not r.is_prime(q)):
    q += 2
  return q
