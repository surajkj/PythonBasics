# Take a number from user and pring all even odd
# Number from one to given range

n = int(input('Please enter a number\n'))

for num in range(1,n+1):
    if num % 2 == 0:
        print(num,'is even number')
    else:
        print(num, 'is odd number')