from datetime import datetime,timedelta

def add_days_to_current_date(days_to_add):
  #Get the current date and time
  current_date=datetime.now()

  #Calculate the new date by adding days_to_add
  new_date=current_date+timedelta(days=days_to_add)

  #Print the result
  print(f"Current Date:{current_date.strftime('%Y-%m-%d%H:%M:%S')}")
  print(f"Date after adding{days_to_add}days:{new_date.strftime('%Y-%m-%d%H:%M:%S')}")

#Example:Adding 5 days to the current date
add_days_to_current_date(5)
