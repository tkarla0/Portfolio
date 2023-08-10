from datetime import datetime
from datetime import timedelta
import calendar

class DateInformation:
  #Initial function which sets number of sides to 6 by default
  def __init__(self): 
    self.date=datetime.now()
    self.new_datetime = self.date- timedelta(hours=4)
    self.cur_month = self.new_datetime.month
    self.month_name = calendar.month_abbr[self.cur_month]
    self.year_cur = self.new_datetime.year
    self.day_cur = self.new_datetime.day
    self.cur_hour = self.new_datetime.hour
    self.cur_min = self.new_datetime.minute
    self.cur_sec = self.new_datetime.second
    if self.cur_hour > 11:
      self.salu="PM"
    else:
      self.salu="AM"
    self.formatDate =  str(self.month_name) + " " +  str(self.day_cur) + ", " + str(self.year_cur) + "  " + str(self.cur_hour) + ":" + str(self.cur_min) + ":" + str(self.cur_sec) + " " + self. salu 



    