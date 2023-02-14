# sum_of_digits
import csv
d = []
with open ('test_numbers.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        d.append(row)
        
def sum_of_digits(n):
    a = list(map(int, n))
    s = sum(a)
    return s

for i in range(0, len(d)):    
    n = d[i][0]
    s = sum_of_digits(n)
    print('Input value:', int(n),'Output result:', s)

