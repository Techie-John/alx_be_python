# Prompt user for pattern size
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Draw the pattern
row_count = 0
while row_count < size:
    for _ in range(size): # Inner loop for columns
        print("*", end="") # Print asterisk without newline
    print() # Print newline after each row
    row_count += 1