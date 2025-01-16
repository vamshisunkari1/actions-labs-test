class EvenFibonacci:
    def __init__(self):
        # Initialize the first two Fibonacci numbers and an empty list to store even Fibonacci numbers
        self.first = 0
        self.second = 1
        self.sum_even_fibonacci = 0
        self.count = 0

    def generate_even_fibonacci(self, limit):
        """Generates Fibonacci numbers and adds the even ones until the limit is reached."""
        while self.count < limit:
            # Calculate the next Fibonacci number
            next_fib = self.first + self.second
            self.first = self.second
            self.second = next_fib
            
            # Only consider even Fibonacci numbers
            if next_fib % 2 == 0:
                self.sum_even_fibonacci += next_fib
                self.count += 1

    def get_sum_of_even_fibonacci(self):
        """Returns the sum of the first 100 even Fibonacci numbers."""
        return self.sum_even_fibonacci


# Example Usage
if __name__ == "__main__":
    fibonacci_calculator = EvenFibonacci()
    
    # Generate the first 100 even Fibonacci numbers
    fibonacci_calculator.generate_even_fibonacci(100)
    
    # Print the result
    print(f"Sum of the first 100 even Fibonacci numbers: {fibonacci_calculator.get_sum_of_even_fibonacci()}")