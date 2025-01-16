class DecimalDigitTransformation:
    def __init__(self, digit):
        """Constructor to initialize the digit."""
        self.digit = digit

    def validate_input(self):
        """Validates if the input is a single digit integer."""
        if not isinstance(self.digit, int):
            raise ValueError("Input must be an integer.")
        if self.digit < 0 or self.digit > 9:
            raise ValueError("Input must be a single digit (0-9).")
    
    def calculate_transformation(self):
        """Calculates the sum of X + XX + XXX + XXXX."""
        self.validate_input()
        
        # Calculating X, XX, XXX, XXXX
        X = self.digit
        XX = int(f"{X}{X}")
        XXX = int(f"{X}{X}{X}")
        XXXX = int(f"{X}{X}{X}{X}")
        
        # Returning the sum
        return X + XX + XXX + XXXX


# Example usage:
if __name__ == "__main__":
    try:
        digit = int(input("Enter a single digit: "))
        transformation = DecimalDigitTransformation(digit)
        result = transformation.calculate_transformation()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")