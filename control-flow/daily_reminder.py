# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += ". Try to complete it soon."
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder_message += " and should be addressed today."
        else:
            reminder_message += ". Consider working on it today."
    case 'low':
        reminder_message = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder_message += ". It's time-bound, so try to get to it today."
        else:
            reminder_message += ". Consider completing it when you have free time."
    case _: # Default case for invalid priority
        reminder_message = "Invalid priority level entered."

# Provide a customized reminder with the exact required format
print(f"Reminder: {reminder_message}")
