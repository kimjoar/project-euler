# What is the smallest number that is evenly divisible by all the numbers from 1 to 20?

def divisable(n):
  return sum([n % i for i in range(1,21)]) == 0

def divisable2(n):
  for i in range(1,21):
    if n % i != 0:
      return False
  return True

# We don't need to check the numbers that divide a number already checked.
# Therefore we don't need to check 5 and 10 since we already must check 20, and
# so on for the other numbers. We therefore only need to check 11 through 20.
def divisable3(n):
  for i in range(11,21):
    if n % i != 0:
      return False
  return True

n = 20
while not divisable3(n):
  n += 20

print n