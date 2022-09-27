# JAWHER ALKOTAIM

'''
Create a running Python project that can take two dates as input, and then
calculate the amount of time between them.
Examples:
Input : 22/2/1970 , 22/2/1980
Output : 10 Years, 0 Months, 0 Days
'''

import re
from datetime import datetime
from dateutil import relativedelta

def calc_time_difference(date1: str, date2: str)-> str:

    date1, date2 = datetime.strptime(date1, '%d/%M/%Y'), datetime.strptime(date2, '%d/%M/%Y')
    difference = relativedelta.relativedelta(date1, date2)

    years = difference.years if difference.years > 0 else difference.years*-1
    months = difference.months if difference.months > 0 else difference.months*-1
    days = difference.days if difference.days > 0 else difference.days*-1

    return f'{years} Years, {months} Months, {days} Days'



try:
 date_extract_pattern = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
 input = input('Input: ')
 example = re.findall(date_extract_pattern, input) # ensures the user enter 2 dates with the right date dd/mm/yyyy formating

 if not example: raise IOError('follow the format dd/mm/yyyy')

 print(f'Output: {calc_time_difference(example[1], example[0])}')

except IOError as e:
    print(e)
except IndexError as e:
    print('you must enter two dates')