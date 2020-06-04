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

my_str = '''Hello World, this is a big line of multiple hello world in this
world hello Hello World
World world wor hello Hello
'''

print(my_str)
print(my_str[3:50])

max_count = int(input("How many Fibonacci numbers do you want? "))
count = 3
previous_num = 0
current_num = 1
if max_count > 0:
  print(previous_num)
if max_count > 1:
  print(current_num)
while count <= max_count:
  tmp = current_num + previous_num
  previous_num = current_num
  current_num = tmp
  print(current_num)
  count += 1
print('Program exited')


'''
Splits a number into Units Tens and Hundreds
'''
number = int(input('Enter a number: '))
run_time = len(str(number))
curr_number = number
output = ''
tmp = 5
for i in range(run_time-1, -1, -1):
  tmp =  curr_number // (10 ** i) * (10 ** i)
  if tmp == 0:
    continue
  output += str(tmp) + ' + '
  curr_number = curr_number % (10 ** i)
output = output[:-3]
print(f'{number} = {output}')