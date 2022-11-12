import makeListOfPrimes as lst
import helperFunctions as arr
import numpy as np
import random

list_of_primes = lst.get_list_of_primes()

#returns true iff n is coprime to the first pi primes
def is_co_prime(n, pi):
  return arr.every(list_of_primes[:pi], lambda p: n % p != 0)

def rand_co_prime(n, pi):
  q = 0
  t = 0
  while(not is_co_prime(q, pi) and t < 100):
    q = random.randint(2**(n-1), 2**n)
    t += 1
  return q

def is_prime(n):
  if n in list_of_primes:
    return True
  return False

  #returns a random odd integer between 2^n-1 and 2^n
def rand_odd(n):
  q = 0
  while(q % 2 == 0):
    q = random.randint(2**(n-1), 2**n)
  return q

def rand_theta(n):
  array = []
  for i in range(0, n):
    array.append(arr.map([-1] * n, lambda x: random.randint(0, 1)))
  return arr 

def rand_seq(n):
  array = []
  for i in range(0, n):
    array.append(arr.map([-1] * n, lambda x: random.randint(2**(n-1), 2**n-1)))
  return array
