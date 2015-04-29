#!/usr/bin/env python
#coding=utf-8

import time
import datetime, calendar
import dateutil

last_friday = datetime.date.today()
one_day = datetime.timedelta(days=1)

# Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example
while last_friday.weekday() != calendar.FRIDAY:
    last_friday -= one_day
    
print last_friday.weekday(), calendar.FRIDAY


