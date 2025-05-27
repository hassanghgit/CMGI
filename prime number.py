# prompt: calaulate the mod of three digit prime number(choose on your own) to 2 and proof that it is True

# We choose 101 as a three-digit prime number.
prime_number = 101
mod_result = prime_number % 2

print(f"The prime number is: {prime_number}")
print(f"The modulo 2 result is: {mod_result}")

# Proof:
# A prime number greater than 2 must be odd.
# An odd number divided by 2 always has a remainder of 1.
# Therefore, the modulo 2 of a three-digit prime number will be 1.
# Since 1 is a non-zero value, it is considered "True" in a boolean context.

is_true = bool(mod_result)
print(f"Is the modulo result True?: {is_true}")

# We can also check if the number is prime (optional but good practice)
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

print(f"Is {prime_number} a prime number?: {is_prime(prime_number)}")
print(f"Is {prime_number} a three-digit number?: {100 <= prime_number <= 999}")