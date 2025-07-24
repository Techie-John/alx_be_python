from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Returning for potential use in calculate_future_date if needed

def calculate_future_date(start_date: datetime):
    """
    Calculates a future date based on user input.

    Args:
        start_date (datetime): The starting date from which to calculate the future date.
    """
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
        return

    future_date = start_date + timedelta(days=num_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    current_dt = display_current_datetime()
    calculate_future_date(current_dt)