import time
import numpy as np
import random
start_time = time.time()

def reduce(arr, func, init):
  acc = init
  for elem in arr:
    acc = func(acc, elem)
  return acc
  
def map(arr, func):
  ret = []
  for elem in arr:
    ret.append(func(elem))
  return ret

def filter(arr, func):
  ret = []
  for elem in arr:
    if func(elem):
      ret.append(elem)
  return ret

def every(arr, func):
  for elem in arr:
    if not func(elem):
      return False
  return True

def some(arr, func):
  for elem in arr:
    if func(elem):
      return True
  return False

def forEach(arr, func):
  for elem in arr:
    func(elem)

# def ptest(n):
#   c = 2
#   lst = []
#   prime = True

#   while(len(lst) < n):
#     for i in lst:
#       if (c % i == 0):
#         prime = False
#     if (prime):
#       lst.append(c)
#     prime = True
#     c+=1
#   return lst

# #returns true iff n is coprime to the first pi primes
# def coprime(n, pi):
#   cop = True
#   for i in listofprimes[:pi]:
#     if (n % i == 0 or i % n == 0):
#       cop = False
#   return cop


def writeprimes(n):
  with open('C:/Users/ibzim/OneDrive - University of Massachusetts/Computer Science/Python/Prime Project/primes.txt', 'w') as f:
    f.write(str(2))
    f.write('\n')
    p = 3
    lst = []
    prime = True

    while(len(lst) < n):
      for i in lst:
        if (p % i == 0):
          prime = False
      if (prime):
        lst.append(p)
        f.write(str(p))
        f.write('\n')
      prime = True
      p+=2

      
def getlistofprimes():
  with open('C:/Users/ibzim/OneDrive - University of Massachusetts/Computer Science/Python/Prime Project/primes1.txt', 'r') as f:
    return map(str.split(f.read()), lambda s: int(s))

listofprimes = getlistofprimes()

def isprime(n):
  if n in listofprimes:
    return True
  return False

# numpy vs random 

#returns a random odd integer between 2^n-1 and 2^n
def randodd(n):
  q = 0
  while(q % 2 == 0):
    q = random.randint(2**(n-1), 2**n)
  return q

#returns true iff n is coprime to the first pi primes
def coprime(n, pi):
  return every(listofprimes[:pi], lambda p: n % p != 0)

def randcoprime(n, pi):
  q = 0
  t = 0
  while(not coprime(q, pi) and t < 100):
    q = random.randint(2**(n-1), 2**n)
    t += 1
  return q



def nprime(n):
  rtime = time.time()
  q = randodd(n)
  t = 0
  while(not isprime(q)):
    q = randodd(n)
    t += 1
  print("nprime trails: ", t)
  print("nprime time in µs: ", (time.time() - rtime) * 1000000)
  return q

def nprime2(n):
  rtime = time.time()
  q = randodd(n)
  t = 0
  while(not isprime(q) or t > 100):
    q += 2
    t += 1
  print("nprime2 trails: ", t)
  print("nprime2 time in µs: ", (time.time() - rtime) * 1000000)
  return q

def clprime(n):
  rtime = time.time()
  pi = 4
  prod = reduce(listofprimes[:pi], lambda acc, elem: acc*elem, 1)
  q = randcoprime(n, pi)
  t = 0
  while(not isprime(q) or t > 100):
    q += prod
    t += 1
  print("clprime trails: ", t)
  print("clprime time in µs: ", (time.time() - rtime) * 1000000)
  return q



a = nprime(23)
print(a)
print(isprime(a))
print('')

a = nprime2(23)
print(a)
print(isprime(a))
print('')

a = clprime(23)
print(a)
print(isprime(a))
print('')

print("--- %s seconds ---" % ((time.time() - start_time)))
