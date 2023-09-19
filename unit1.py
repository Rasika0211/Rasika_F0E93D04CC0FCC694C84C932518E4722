#1.2 Leap year 

def isleapYear(year):
     if (year%4==0and year % 100 != 0) or year %  400==0:
      return True
     else:
        return False 
       
Year = 2012 

if (Year):
  print('{} is a leap year.'.format(Year))
else:
     print('{} is not a leap year.'.format(Year))