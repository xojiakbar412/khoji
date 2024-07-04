class Fibonacci:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.a - self.b


max_value = 100 
fib = Fibonacci(max_value)

for number in fib:
    print(number)
