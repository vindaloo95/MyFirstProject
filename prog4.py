'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''
def count_evens(nums):
  count = 0
  for i in (nums):
    if i % 2 == 0:
      count +=1
  return count

'''

Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

'''
def big_diff(nums):
  nums.sort()
  return nums[-1] - nums[0]

'''

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

'''

def sum13(nums):
  sum = 0
  skip = False
  for i in nums:
    if i == 13:
      skip = True
    elif skip:
      skip = False
    else:
      sum += i
  return sum

'''


Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''
def sum67(nums):
  sum = 0
  skip = False
  for i in nums:
    if i == 6:
      skip = True
    elif skip and i == 7:
      skip = False
    elif skip:
      pass
    else:
      sum += i
  return sum

'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''

def has22(nums):
  
  leng = len(nums) - 1
  for index,i in enumerate(nums):
    if index != leng:
      if i == 2 and nums[index+1] == 2:
        return True
  return False


'''

The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

'''

Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8

'''

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b

def pascal(line_count):
  if line_count > 0:
    print('1')
  if line_count > 1:
    print('1 1')
  if line_count > 2:
    t = (1,1)
    for i in range(2,line_count):
      l = []
      end = len(t) - 1
      for j in range(len(t)):
        if j == 0:
          l.append(t[j])
        elif j == end:
          l.append(t[j])
          break
        l.append(t[j] + t[j+1])
      str1 = ''
      for i in l:
        str1 = str1 + ' ' + str(i)
      print(str1.strip())
      t = tuple(l)

print(pascal(10))


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

def armstrong(num):
  str_num = str(num)
  n = len(str_num)
  sum = 0
  for x in str_num:
    sum += int(x) ** n
  if (sum == num):
    return True
  else:
    return False
  
for i in range(10001):
  if (armstrong(i)):
    print(i)


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

'''Alternative method '''
number = input('Enter a number: ')
l = list(number)[::-1]
output = ''
for i in range(len(l)-1, -1, -1):
  tmp = str(int(l.pop()) * 10 ** i)
  if tmp != '0':
    output += tmp + " + "
output = output[:-3]
print(f'{number} = {output}')
'''
Prime or not
'''
number = 13
is_prime = False
for i in range(2, number):
  print(i, number % i)
  if number % i == 0:
    break
else:
  is_prime = True
if is_prime:
  print(f'The number {number} is Prime')
else:
  print(f'The number {number} is NOT Prime')

def greeting(name):
    print(f'Hello welcome to Python class Mr.{name}')


def calculate(list1):
    """This is addition"""
    sum = 0
    for i in list1:
        sum += i
    return sum


def multiplication(l1):
    multiplication = 1
    count = 0
    for i in l1:
        if i != 0:
            count += 1
            multiplication *= i
    if count == 0:
        return 0
    else:
        return multiplication


def count_even_and_odd_numbers(my_list):
    even_count = 0
    odd_count = 0
    for i in my_list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count




# list1 = [1, 2, 5, 3, 6, 0, 7, 0, 0, 5, 0, 4]
list1 = [1,3,5,15,9,10,21,25,30,45]

list2 = [2, 2, 0]
list3 = [4, 6, 8, 3, 14, 18, 12, 6]


def count_mul3_mul5(list1):
    mul3 = 0
    mul5 = 0
    for i in list1:
        if i == 0:
            continue
        if i % 3 == 0:
            mul3 += 1
        elif i % 5 == 0:
            mul5 += 1
    return mul3,mul5


mul3, mul5 = count_mul3_mul5(list1)
print(list1)
print(f'Mul 3 count: {mul3}, Mul 5 count: {mul5}')

mul3, mul5 = count_mul3_mul5(list2)
print(list2)
print(f'Mul 3 count: {mul3}, Mul 5 count: {mul5}')

mul3, mul5 = count_mul3_mul5(list3)
print(list3)
print(f'Mul 3 count: {mul3}, Mul 5 count: {mul5}')

'''
Have a list of numbers:  Return the difference between the highest and lowest value in that list

Add all the numbers in the array....if there is a number 9, you need to ignore that number and the following number:

[1, 5, 9, 2, 3, 4, 9, 2, 1] = 14

Give you a list... add all the numbers, but if see 10...ignore that number and the next 5 numbers. give the sum as a return value

[5,10,15,2,3,4,6,6,7,10,11]
5 + 6 + 7 = 18
'''


def diff_high_low(my_list):
    my_list.sort()
    return my_list[-1] - my_list[0]


l1 = [15,43,12,21,45,23,98,46,87,38]
print(diff_high_low(l1))

def ignore9(my_list):
    sum = 0
    skip = False
    for i in my_list:
        if i == 9:
            skip = True
        elif skip:
            skip = False
        else:
            sum += i
    return sum
l1 = [1, 9, 9, 3, 3, 4, 9, 2, 1]
print(ignore9(l1))


def ignore10_and_next5(my_list):
    sum = 0
    skip = False
    count = 0
    for i in my_list:
        if i == 10:
            skip = True
            count = 0
        elif skip:
            count += 1
            if count == 5:
                skip = False
        else:
            sum += i
    return sum
l1 = [5,10,15,2,3,4,6,6,7,10,11]
print(ignore10_and_next5(l1))