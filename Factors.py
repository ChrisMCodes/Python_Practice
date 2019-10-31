your_num = input('Please enter a valid integer: ' )

while True:
    try:
        your_num = int(your_num)
        break
    except:
        your_num = input("Your input doesn't seem to have worked. Please enter a valid integer: ")
        continue

print('Your number is:', your_num)


facts = []
for i in range(1, your_num+1):
    if your_num % i == 0:
        facts = facts + [i]
factual = 'The factors of {} are {}'.format(your_num, facts)
print(factual)
