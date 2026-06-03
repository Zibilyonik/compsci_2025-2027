import csv

from io import StringIO
data = "x,y\nx,y\nx, y"
r = csv.reader(StringIO(data))
for row in r:
  print(row) 

