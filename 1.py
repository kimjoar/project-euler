# Add all the natural numbers below one thousand that are multiples of 3 or 5

# Solution 1
print sum([i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0])

# Solution 2
print sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, xrange(1000)))

# Solution 3
total = 0
for i in xrange(1000):
  if i % 3 == 0 or i % 5 == 0:
    total += i
print total