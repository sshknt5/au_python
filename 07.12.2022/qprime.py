def isprime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True


print(isprime(6))
