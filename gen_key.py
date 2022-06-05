import random 

numbers = 'a1b2c4e56h8i9l'

for i in range(100):
    key = ''.join(random.choice(numbers)for i in range(10))
    print(key)