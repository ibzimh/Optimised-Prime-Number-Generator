def getlistofprimes():
  with open('C:/Users/ibzim/OneDrive - University of Massachusetts/Computer Science/Python/Prime Project/primes1.txt', 'r') as f:
    return map(str.split(f.read()), lambda s: int(s))

def map(arr, func):
  ret = []
  for elem in arr:
    ret.append(func(elem))
  return ret

print(getlistofprimes()[999999])