#1
import time
import sys

powt=1000
N=10000

def tester(f):
  start = time.time_ns()
  f()
  stop = time.time_ns()
  return stop-start

def forStatement():
  l = []
  for i in range(N):
    l.append(i)
  # s = 0
  # for i in l:
  #   s += i
  # sum(l)
  
def listComprehension():
  l = [i for i in range(N)]
  # s = 0
  # for i in l:
  #   s += i
  # sum(l)

def mapFunction():
  m = map(lambda x: x, range(N))
  # m = list(map(lambda x: x, range(N)))
  # s = 0
  # for i in m:
  #   s += i
  # sum(m)


def generatorExpression():
  g = (i for i in range(N))
  # g = list((i for i in range(N)))
  # s = 0
  # for i in g:
  #   s += i
  # sum(g)

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
# for testFunction in test:
    # print(testFunction.__name__.ljust(20), '=>', tester(testFunction))


#2
import random

l1 = [random.randrange(0,20) for _ in range(100)]
l2 = [random.randrange(0,20) for _ in range(100)]
l12 = list(filter(lambda x: 3<sum(x)<15, zip(l1,l2)))
# print(l12)

#3
import math

def fit(x,y):
  n = len(x)
  x_sr = sum(x)/n
  y_sr = sum(y)/n
  D = sum(map(lambda xi:(xi-x_sr)**2, x))
  a = sum(map(lambda xi, yi: yi*(xi-x_sr), x, y))/D
  b = y_sr-a*x_sr
  delta_y = math.sqrt(sum(map(lambda xi, yi: (yi-(a*xi+b))**2, x, y))/(n-2))
  delta_a = delta_y/math.sqrt(D)
  delta_b = delta_y*math.sqrt(1/n+x_sr**2/D)
  return a,b, delta_a, delta_b

x = [i for i in range(100)]
y = [15*xi+3 for xi in x]
print(fit(x,y))

#4

def myreduce(f,s):
  x = f(s[0], s[1])
  for i in range(2,len(s)):
    x = f(x, s[i])
  return x

s = [1,2,3,4,5]
print(myreduce(lambda x,y: x+y, s))
print(myreduce(lambda x,y: x*y, s))
