class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        while not self.is_prime(self.num):
            self.num += 1
            if self.num > self.limit:
                raise StopIteration
        return self.num

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


limit = 30
prime_iterator = PrimeIterator(limit)
for prime in prime_iterator:
    print(prime)



limit = 30
prime_iterator = PrimeIterator(limit)
for prime in prime_iterator:
    print(prime)

###gen

def prime_generator(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


limit = 30
for prime in prime_generator(limit):
    print(prime)
