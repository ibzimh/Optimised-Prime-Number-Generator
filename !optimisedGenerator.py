import numpy as np
import random
import helperFunctions as arr
import makeListOfPrimes as lst
import primeHelpers as r
import compositeTest as comp

listofprimes = lst.get_list_of_primes()

# returns the product of the first k prime with random small exponents
def prodprimes(k):
  # the array of exponents (eq 1, 1)
  exp = arr.map([-1] * k, lambda x: random.randint(1, 7))

  # array of a small prime numbers raised to the ith exponent from exp (eq 1, 2)
  p = arr.map_ind(listofprimes[:k], lambda x, ind: x ** exp[ind])

  # the prod of all primes^exp's in p (eq 1, 3)
  prod = arr.reduce(p, lambda acc, e: acc*e, 1)

  # largest prime^exp in p (eq 2, 1)
  maxp = np.amax(p)

  # t is the largest prime^exp * a constant (eq 2, 2)
  C = 2
  t = C * maxp

  # an array of k random sequences
  alpha = r.rand_seq(k)

  # an array of k sequences of 0's with 1 at the ith position
  theta = r.rand_theta(k)

  c = 0
  for i in range(0, k):
    rand_int = random.randint(0, k-1) 

    # alpha i (eq 3, 1)
    alfi = alpha[rand_int] 
    # theta i (eq 3, 2)
    theti = theta[rand_int]

    # alpha i raised to the power exp (eq 3, 3)
    alfidelta = np.power(alfi, exp)

    # alpha i ^ delta i * theta i (eq 3, 4) 
    adt = np.multiply(alfidelta, theti)
    
    # the modular dot product 
    dot_product = r.mod_dot_product(adt, p)
    
    # repeat the process again
    if(dot_product == 0):
      i -= 1
    else:
      # adt without the exponents 
      c += r.mod_dot_product(np.multiply(alfi, theti), p)

  return c

# NOT complete 
def gen():
  n = 'b16bd1e084af628fe5089e6dabd16b5b80f60681d6a092fcb1e86d82876ed71921000bcfdd063fb90f81dfd07a021af23c735d52e63bd1cb59c93cbb398afd'
  n = int(n, 16)
  prod = 1729 * n
  rho = 4180 * n
  old_c = prodprimes(512)
  c = old_c
  k = 0
  
  # q is the prime candidate
  q = c + rho
  
  # while not prime
  while(not comp.miller_deterministic(q)):
    c *= old_c
    q = c + rho
  return c
