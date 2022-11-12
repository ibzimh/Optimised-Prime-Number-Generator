def reduce(arr, func, init):
  acc = init
  for elem in arr:
    acc = func(acc, elem)
  return acc

def reduceind(arr, func, init):
  acc = init
  for ind, elem in enumerate(arr):
    acc = func(acc, elem, ind)
  return acc
  
def map(arr, func):
  ret = []
  for elem in arr:
    ret.append(func(elem))
  return ret

def mapind(arr, func):
  ret = []
  for ind, elem in enumerate(arr):
    ret.append(func(elem, ind))
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