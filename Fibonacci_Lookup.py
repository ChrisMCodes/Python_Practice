#This program finds the Fibonacci number at a given index
#For these purposes, index 0 = 0, index 1 = 1, index 2 = 1, index 3 = 2, and so on

fib = []
x = int(input('Index to look up: '))
ind = []

for i in range(x+1):
  if len(ind) == 0:
    ind = ind + [0]
  else:
    ind = ind + [ind[i-1]+1]
#print(ind) #Test



for i in ind:
  if i < 2:
    fib = [0, 1]
  else:
    fib.append((fib[i-2]+fib[i-1]))

ans = fib[-1]
print('The Fibonacci number at index {} is {}.'.format(x, ans))
