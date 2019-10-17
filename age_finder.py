from datetime import date


def calculate_age(birth_date):
    todays_date = date.today()
    calculated_age = todays_date.year - birth_date.year - ((todays_date.month, todays_date.day)
                                                           < (birth_date.month, birth_date.day))
    return calculated_age


print('Enter your birth date details to know your age :')
day = int(input("Enter the day:"))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(calculate_age(date(year, month, day)), "years")
