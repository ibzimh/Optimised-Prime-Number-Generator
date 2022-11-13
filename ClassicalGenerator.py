import Main as main
import numpy as np
import makeListOfPrimes as lst
import random
import helperFunctions as arr
import primeHelpers as r

listofprimes = lst.get_list_of_primes()

def clprime(n):
  pi = 4
  
  # product of the first few (pi) primes 
  prod = arr.reduce(listofprimes[:pi], lambda acc, elem: acc*elem, 1)
  
  # this takes the idea of the naive generator checking for non-evens and uses it to filter out more numbers.
  
  # a random number in the range which is coprime to pi
  q = r.rand_co_prime(n, pi)
  while(not r.is_prime(q)):
    q += prod
  return q
