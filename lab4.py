#1
import random
k = 100
l = []
for i in range(k):
  l.append(random.randrange(0,5*k))
w = dict.fromkeys(range(k//10),0)
for i in range(100):
  l2 = l[:]
  random.shuffle(l2)
  s = 0
  for i in range(k):
    if l[i] == l2[i]:
      s += 1
  w[s] += 1
  l = l2[:]
print(w)

#2
letters = {}
for i,j in enumerate('qwertyuiopasdfghjklzxcvbnm'):
  letters[i] = j
string = ''
for i in range(k):
  string = '.'.join([string, letters.get(random.randint(0,25))])
print(string)

#3
los = []
for i in range(100):
  los.append(random.randrange(0,20))
print(los)
#3a
count = {}
for i,j in enumerate(los):
  count.setdefault(j,[]).append(i)
# print(count) 
#3b
count = {}
l = []
for i in los:
  p = count.get(i)[-1] + 1 if count.get(i) else 0
  count.setdefault(i,[]).append(los.index(i, p))
# print(count) 

#4
n = 3
palindroms = {}
for n in range(3,7):
  l = []
  s = 0
  for i in range(1000):
    l.append(random.randrange(10**(n-1), 10**n))
  for i in l:
    if i//10**(n-1) == i%10 and i//10**(n-2)%10 == i//10%10 and i//10**(n-3)%10 == i//100%10:
      s += 1
  palindroms[n] = s

print(palindroms)

#5
s1 = {}
s2 = {}
for i in range(10):
  s1[i] = random.randrange(1,100)
  s2[i] = random.randrange(1,100)
# print(s1,s2)

s1_new = {}
s2_new = {}
for i in s1:
  s1_new[s1.get(i)] = i
  s2_new[s2.get(i)] = i
print(s1_new,s2_new)

s12 = {k:(s1.get(k),s2.get(k)) for k in s1 if k in s2}
print(s12)


