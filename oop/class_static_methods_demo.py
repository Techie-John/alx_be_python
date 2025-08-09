class Calculator:
    """A calculator class demonstrating class and static methods."""
    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not require access to class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It uses the 'cls' parameter to access a class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b