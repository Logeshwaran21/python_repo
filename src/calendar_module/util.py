import calendar
import datetime
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def calendar_module():
    date_str = input("Enter a date (MM-DD-YEAR): ")
    month, day, year = map(int, date_str.split('-'))
    day_of_week = datetime.date(year,month,day).weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    logging.debug(f"The day on, {date_str}, is, {days_of_week[day_of_week]}")