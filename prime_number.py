def is_prime(num):
    # Check if the number is less than 2
    if num <= 1:
        return False
    
    # Check for numbers 2 and 3 explicitly
    if num <= 3:
        return True
    
    # Check if the number is divisible by 2 or 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check for prime numbers of the form 6k ± 1 up to sqrt(num)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
number = 29
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
