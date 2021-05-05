def fun1(name, n): 
  with open(name) as pl1:
    file = pl1.readlines()
    wiersze_pocz = file[:n]
    wiersze_kon = file[-n:]
    n_lin = file[::n]
    znaki = [s[n] for s in file if len(s)>n]
    slowa = [s.split(" ")[n] for s in file]
    print(wiersze_pocz)
    print(wiersze_kon)
    print(n_lin)
    print(znaki)
    print(slowa)

fun1("test.txt", 2)

import glob
import numpy

def fun2(files):
  data = [[] for _ in range(50)]
  for f in files:
    i = 0
    with open(f) as file:
      for line in file:
        data[i].append((float)line)
        i += 1
  with open("zad2.txt", "w") as z:
    for i in range(50):
      z.write(f'{i} {numpy.average(data[i])} {numpy.std(data[i])}\n')
    
files = glob.glob("./data/data*in")
# print(files)
fun2(files)

def fun3():
  with open("zad3.py", "w") as file:
    
  


    file.write(
      '''import numpy
      x,y=numpy.loadtxt('zad2.txt', unpack=True)
      import matplotlib.pyplot as plt
      plt.plot(x, y, 'o')
      plt.errorbar(x, y, marker='*', yerr=dy)
      plt.xlabel('x')
      plt.savefig('res.pdf')''')
fun3()



def fun4_b(files):
  g_dict = dict()
  
  for file in files:
    surname_rank = dict()
    file_key = int(file.split('.')[0])
    with open(file, 'r') as f:
      for line in f:
        items_list = line.split()
        surname_rank[items_list[0]] = items_list[1]
      g_dict[file_key] = surname_rank


  for k, v_dict in g_dict.items():
    print(f'{k} -> ')
    for surname, rank in v_dict.items():
      print(f'{surname} = {rank}')



def fun4(files):
  data = [["Nazwisko"]]
  for i in range(2000,2021):
    data[0].append(i)
  i = 0
  for f in files:
    with open(f) as file:
      for line in file:
        line = line.split(" ")
        if(line[0] not in data):
          data.append([line[0]])
          data[len(data)-1].extend(["-"]*i)
          data[len(data)-1].append(line[1])
        else:
          for d in data:
            if d[0]==line[0]:
              d.append(line[1])
    i += 1
  with open("rank.out", "w") as r:
    for d in data:
      r.write(f"{d}\n")


files = glob.glob("./rank/*")
#fun4(files)
fun4_b(files)

def fun5(files):
  hist = {}
  for f in files:
    with open(f) as file:
      for line in file:
        line = line.split(" ")
        for s in line:
          hist.setdefault(s[0], []).append(s)
  print(hist)

files = glob.glob("zad5*in")
fun5(files)
