import sys

if len(sys.argv) < 2:
  print("Prosze wywolac program nastepujaco: python3 lab3.py elementy wywolania")
  sys.exit()
else:

  s = ' '.join(sys.argv[1:])
  print(s)
  
  lower = [i for i in s if i.islower()]
  upper = [i for i in s if i.isupper()]
  numbers = [i for i in s if i.isdecimal()]
  other = [i for i in s if not i.isalnum()]

  print(lower)
  print(upper)
  print(numbers)
  print(other)

  lower_limited = []
  for l in lower:
    if l not in lower_limited:
      lower_limited.append(l)
  print(lower_limited)

  lower_count = [(i, lower.count(i)) for i in lower_limited]
  lower_count.sort(key=lambda x: x[1], reverse=True)
  print('Sortowanie po krotności: ', lower_count)

  a = sum(s.count(i) for i in 'aeuyio')
  b = 0
  for i in s:
    if i.isalpha():
      b += 1
  b -= a

  lin_fun = [(int(i), a * int(i) + b) for i in numbers]
  print(f'{a=}, {b=}:', lin_fun)

  x = [i for (i,j) in lin_fun]
  y = [j for (i,j) in lin_fun]
  x_sr = sum(x)
  x_sr /= len(x)
  
  d = sum(pow((i - x_sr), 2) for i in x)

  a_obl = sum(yi * (xi - x_sr) for (xi,yi) in lin_fun)
  a_obl /= d
  
  y_sr = sum(y)
  y_sr /= len(y)
  b_obl = y_sr - a_obl*x_sr
  
  print(f'{x_sr=}, {d=}, {y_sr=}')
  print(f'{a_obl=}, {b_obl=}')

    

