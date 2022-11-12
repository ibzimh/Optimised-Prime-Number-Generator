import helperFunctions as arr

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

def import_list_of_primes():
  with open('C:/Users/ibzim/OneDrive - University of Massachusetts/Computer Science/Python/Prime Project/primes1.txt', 'r') as f:
    return arr.map(str.split(f.read()), lambda s: int(s))

listofprimes = import_list_of_primes()

def get_list_of_primes():
  return listofprimes