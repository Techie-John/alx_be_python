# Prompt user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Generate and print the multiplication table
for i in range(1, 11): # Loops from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")
    