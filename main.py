def getFibonnaciSeries(num):
  c1, c2 = 0, 1
  count = 0
  while count < num:
    yield c1
    c3 = c1 + c2
    c1 = c2
    c2 = c3
    count += 1

fin = getFibonnaciSeries(5)
print(fin)
for i in fin:
  print(i)