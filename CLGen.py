import Main as main
import numpy as np
import makeListOfPrimes as lst
import random
import helperFunctions as arr
import helpers as r

listofprimes = lst.get_list_of_primes()

def clprime(n):
  pi = 4
  prod = arr.reduce(listofprimes[:pi], lambda acc, elem: acc*elem, 1)
  q = r.rand_co_prime(n, pi)
  t = 0
  while(not r.is_prime(q) or t > 100):
    q += prod
    t += 1
  print("clprime trails: ", t)
  return q