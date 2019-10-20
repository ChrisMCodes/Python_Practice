num_rows = int(input('Please enter the highest positive integer to multiply by in your table: '))
rows = []
for um_row in range(1, num_rows+1):
    rows = rows + [um_row]

#Creates a clone of rows as a cross multiplier
nums = rows[:]

for row in rows:
    for num in nums:
        print('{:5}'.format(num*row), end='')
    print('\n')

