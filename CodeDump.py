# numpy vs random 


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




# print(prodprimes(10))



# res = prodprimes(16)
# print(res)
# print(isprime(res))





# a = nprime(23)
# print(a)
# print(isprime(a))
# print('')

# a = nprime2(23)
# print(a)
# print(isprime(a))
# print('')

# a = clprime(23)
# print(a)
# print(isprime(a))
# print('')

# s = [0, 0, 0]
# t = [0, 0, 0]
# n = 30

# for i in range(0, n):
#   s[0] += nprime(23)[0] 
#   s[1] += nprime2(23)[0]
#   s[2] += clprime(23)[0]
#   t[0] += nprime(23)[1]
#   t[1] += nprime2(23)[1]
#   t[2] += clprime(23)[1]

# s = map(s, lambda x: x/n)
# t = map(t, lambda x: x/n)
# forEach(s, lambda x: print('time in ms: ', x))
# print()
# forEach(t, lambda x: print('trials: ', x))