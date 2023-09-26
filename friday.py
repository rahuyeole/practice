import datetime

def has_13th_friday(month, year):
    try:
        
        date = datetime.date(year, month, 13)
        
       
        day_of_week = date.weekday()
        
        
        return day_of_week == 4
    except ValueError:
        
        return False


try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (4 digits): "))

    if 1 <= month <= 12 and len(str(year)) == 4:
        result = has_13th_friday(month, year)
        if result:
            print(f"Friday the 13th exists in {datetime.date(year, month, 1).strftime('%B')} {year}.")
        else:
            print(f"No Friday the 13th in {datetime.date(year, month, 1).strftime('%B')} {year}.")
    else:
        print("Invalid input. Month should be between 1 and 12, and year should be a 4-digit number.")
except ValueError:
    print("Invalid input. Please enter valid numeric values for month and year.")
