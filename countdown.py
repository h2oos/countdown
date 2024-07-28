from datetime import datetime, timedelta

def countdown(target_date):
    # Get the current date and time
    now = datetime.now()
    
    # Calculate the difference between the target date and now
    time_remaining = target_date - now
    
    if time_remaining < timedelta(0):
        return "The target date has already passed!"
    
    # Calculate days, hours, minutes, and seconds
    days = time_remaining.days
    seconds = time_remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    
    return f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Set your target date here
target_date_str = '2024-12-31 23:59:59'
target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')

# Get the countdown message
countdown_message = countdown(target_date)

# Print the countdown message
print(countdown_message)
