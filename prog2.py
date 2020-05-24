def temp():
  str1 = "HeLLisfoiKDJFOkfjlkjsLIDfjello World"
  print(str1.capitalize())

  print(str1.count("Hello"))
  print(str1.upper())
  print(str1.lower())

def palindrome(str):
  if len(x) == 1:
    return 'Need more than 1 character'
  y = x[::-1]
  if x == y:
    return "Palindrome"
  else:
    return "Not a palindrome"

x = input("Enter text or number: ")
print(palindrome(x))

###############

#Armstrong number
# The sum of power of individual digits is equal to number itself

num = input('Enter a number: ')
n = len(num)
sum = 0
for x in num:
  sum += int(x) ** n
if (sum == int(num)):
  print(f'The number {num} is an Armstrong number')
else:
  print(f'The number {num} is NOT an Armstrong number')

# getFibonnaciSeries
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

###########

