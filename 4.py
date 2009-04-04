# Find the largest palindrome made from the product of two 3-digit numbers.

# Solution 1
def isPalindrome(number):
  return (str(number) == str(number)[::-1])

# Solution 2
def isPalindrome2(number):
  number = str(number)
  length = len(number)
  
  for i in range(length / 2):
    if number[i] != number[length - (i + 1)]:
      return False

  return True

# Performs computation

largest = 0
for i in xrange(100, 1000):
  for j in xrange(100, 1000):
    if isPalindrome(i * j) and i * j > largest:
      largest = i * j

print largest

# I initially thought that isPalindrome2 would be faster than isPalindrome, but
# to my suprise isPalindrome is faster (atleast on the machine I tested it on).
# On the other hand it performs slower than isPalindrome2 if I do:
#   return (number == int(str(number)[::-1]))