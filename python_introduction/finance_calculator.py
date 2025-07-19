# Prompt the user for their monthly income.
# The input() function gets user input as a string.
# float() is used to convert the string input to a floating-point number,
# allowing for decimal values in income.
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses.
# Similar to income, expenses are converted to a float.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings by subtracting expenses from income.
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate as a decimal.
# 5% is 0.05 in decimal form.
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# First, calculate savings over 12 months without interest.
savings_before_interest = monthly_savings * 12
# Then, calculate the interest earned on those 12 months of savings.
interest_earned = savings_before_interest * annual_interest_rate
# Finally, add the interest earned to the savings before interest to get projected savings.
projected_annual_savings = savings_before_interest + interest_earned

# Display the user's monthly savings.
# Using an f-string for clear and concise output formatting.
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for two decimal places

# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.") # .2f for two decimal places
