def g1():
  l = [1]
  yield l, sum(l)
  l.append(1)
  yield l, sum(l)
  i = 1
  while 1:
    if i > 5:
      return
    l2 = [l[i]+l[i+1] for i in range(len(l)-1)]
    l2.insert(0,1)
    l2.append(1)
    l = l2
    i += 1
    yield l, sum(l)

for g in g1():
  print(g)

#2
import random
N = 20
z = [random.randrange(10)%2 for _ in range(N)]
print(z)

def g2(s):
  count = 0
  one = False
  for i in s:
    if(not i and one):
      one = False
      count = 1
    elif(not i and not one):
      count += 1
    else:
      one = True
      if(count):
        yield count

s = sum(g2(z))
n = len(list(g2(z)))
s /= n
print(s)

#3

def fib():
  a = 1
  yield a
  b = 1
  yield b
  # i = 1
  while 1:
    # if(i>7):
    #   return
    a, b = b, a+b
    # i += 1
    yield b

# for f in fib():
#   print(f)

def par(s, p=True):
  for i in s:
    if(i%2 and not p):
      yield i
    elif(not i%2 and p):
      yield i

l = [random.randrange(20) for _ in range(10)]
# for g in par(l):
#   print(g)

def lessThan(s, max):
  for i in s:
    if(i > max):
      return
    else:
      yield i

# for g in lessThan(range(10), 5):
#   print(g)

sum1 = sum(par(lessThan(fib(), 99)))
print("Suma liczb parzystych ciągu Fibonacciego mniejszych od 100: ", sum1)
sum2 = sum(par(lessThan(fib(), 99), False))
print("Suma liczb nieparzystych ciągu Fibonacciego mniejszych od 100: ", sum2)
  
#4
def myrange(*a):
  if len(a)==3:
    start = a[0]
    end = a[1]
    step = a[2]
  elif len(a)==2:
    start = a[0]
    end = a[1]
  else:
    start = 0
    end = a[0]
  i = start
  if(step>0):
    while i < end:
      yield i
      i += step
  else:
    while i > end:
      yield i
      i += step

for i in myrange(7,2,-2):
  print(i)
# for i in range(7,2,-2):
  # print(i)

#5
import math
def u():
  u = 0
  x = 1
  a = 0.05
  i = 0
  yield x, u, math.log(x)
  while 1:
    if(x==1.5):
      return
    i += 1
    u = u+a/x
    x = 1+i*a
    yield x, u, math.log(x)

for i in u():
  print(i)