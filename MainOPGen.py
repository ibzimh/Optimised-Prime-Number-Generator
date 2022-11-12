import numpy as np
import random
import CLGen as cl
import helperFunctions as arr
import makeListOfPrimes as lst
import helpers as r

listofprimes = lst.get_list_of_primes()

# returns the product of the first k prime with random small exponents
def prodprimes(k):
  # the array of exponents (eq 1, 1)
  exp = arr.map([-1] * k, lambda x: random.randint(1, 1))

  # array of a small prime numbers raised to the ith exponent from exp (eq 1, 2)
  p = arr.mapind(listofprimes[:k], lambda x, ind: x ** exp[ind])

  # the prod of all primes^exp's in p (eq 1, 3)
  prod = arr.reduce(p, lambda acc, e: acc*e, 1)

  # largest prime^exp in p (eq 2, 1)
  maxp = np.amax(p)

  # t is the largest prime^exp * a constant (eq 2, 2)
  C = 2
  t = C * maxp

  # c = 0

  # an array of k random sequences
  alpha = r.rand_seq(k)

  # an array of k random sequences of 0's and 1's
  theta = r.rand_theta(k)
  print(theta)

  # for i in range(0, k):
  #   alfi = random.choice(alpha) # alpha i
  #   theti = random.choice(theta) # theta i
  #   alfidelta = np.power(alfi, exp[i]) # alpha i raised to the power delta 
  #   print(alfidelta)
  #   print(theti)
  #   adt = np.multiply(alfidelta, theti)
  #   reduce(p, lambda acc, e: adt e)

    # while(alfi**exp[i] % p[i]**exp[i] == 0):
    #   alfi = random.choice(alpha)
    # c += alfi % p[i]**exp[i]

  # return c

prodprimes(10)