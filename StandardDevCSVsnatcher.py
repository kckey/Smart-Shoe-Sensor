import csv
import statistics
csv_file = 'StandWalkDat.csv'

heelval = []
toeval = []
heelphase = []
toephase = []

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        heelval.append(row.get('heelval'))
        toeval.append(row.get('toeval'))
        heelphase.append(row.get('heelphase'))
        toephase.append(row.get('toephase'))
a = 2
b = 3
c = 4
d = 5
e = 6
f = 7
g = 8
h = 9
i = 10
j = 11
k = 12
l = 13
m = 14
n = 15
o = 16

while True:

	arr = [heelval[a], heelval[b], heelval[c],heelval[d], heelval[e], heelval[f],heelval[g], heelval[h], heelval[i],heelval[j], heelval[k], heelval[l],heelval[m], heelval[n], heelval[o]]
	new_arr = [int(n) for n in arr]
    print(statistics.variance(arr))    
	

a = a+15
b = b+15
c = c+15
d = d+15
e = e+15
f = f+15
g = g+15
h = h+15
i = i+15
j = j+15
k = k+15
l = l+15
m = m+15
n = n+15
o = o+15

