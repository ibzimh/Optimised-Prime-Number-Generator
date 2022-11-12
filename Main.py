import time
import numpy as np
import random
import ClassicalGenerator as clg
import helperFunctions as arr
import makeListOfPrimes as lst
import naiveGenerator as ng
import optimisedGenerator as opg

def start_time():
  return time.time() 

def print_time(stime):
  print("--- %s seconds ---" % (time.time() - stime))

start_time = start_time()

# Main

listofprimes = lst.get_list_of_primes()



# End of Main

print_time(start_time)