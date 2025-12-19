class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def modulus(self, a, b):
        return a % b

    def square_root(self, a):
        return a ** 0.5

    def log(self, message):
        print(f"LOG: {message}")

if __name__ == "__main__":
    calc = Calculator()
    print("1 + 2 =", calc.add(1, 2))
