# Find the 10001st prime.

def isprime(n):
  # Not fully correct isprime implementation, e.g. always receives odd numbers.
  # It might be better to implement the sieve of Eratosthenes to solve this 
  # problem more effectively.
  for x in range(3, int(n ** 0.5) + 1, 2):
    if n % x == 0:
      return False
  return True

prime, n, value = 3, 2, 3

while(n < 10001):
  value += 2
  if isprime(value):
    prime = value
    n += 1
    
print prime