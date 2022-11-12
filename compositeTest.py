import numpy as np
import random
import ClassicalGenerator as cl
import helperFunctions as arr
import makeListOfPrimes as lst
import primeHelpers as r

def miller_deterministic(n):
    if (n % 2 == 0):
      # print("Bro??")
      return False

    s = np.floor(np.log(n))
    s = int(s)
    d = n - s

    if (n < 3317044064679887385961981):
      return miller_small_n(n, s, d)

    v1 = n - 2
    v2 = int(2 * (np.log(n) ** 2))
    ub = np.minimum(v1, v2)
    
    for a in range (2, ub+1):
        x = (a ** (d)) % n

        for j in range(0, s):
            y = (x ** 2) % n
            if (y == 1 and x != 1 and x != n - 1):
                return False
            x = y

        if (y != 1):
          return False

    return True

def miller_small_n(n, s, d):
  arange = []
  if (n < 1373653):
    arange = [2, 3]
  elif (n < 9080191):
    arange = [31, 73]
  elif (n < 25326001):
    arange = [2, 3, 5]
  elif (n < 3215031751):
    arange = [2, 3, 5, 7]
  elif (n < 4759123141):
    arange = [2, 7, 61]
  elif (n < 1122004669633):
    arange = [2, 13, 23]
  elif (n < 2152302898747):
    arange = [2, 3, 5, 7, 11]
  else: # 3,474,749,660,383
    arange = [2, 3, 5, 7, 11, 13]
  if (n >= 3474749660383):
    arange.append(17)
  if (n >= 341550071728321):
    arange.append(19)
    arange.append(23)
  if (n >= 3825123056546413051):
    arange.append(29)
    arange.append(31)
    arange.append(37)
  if (n >= 318665857834031151167461):
    arange.append(41)
  
  for a in arange:
    x = (a ** (d)) % n

    for j in range(0, s):
        y = (x ** 2) % n
        if (y == 1 and x != 1 and x != n - 1):
          print(n)
          return False
        x = y

    if (y != 1):
      print(n)
      return False

  return True
  
