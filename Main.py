import time
import numpy as np
import random
import CLGen as clg
import helperFunctions as arr
import makeListOfPrimes as lst
import naiveGen as ng

def start_time():
  return time.time() 

def print_time(stime):
  print("--- %s seconds ---" % (time.time() - stime))

start_time = start_time()

# Main

listofprimes = lst.get_list_of_primes()

# End of Main

print_time(start_time)