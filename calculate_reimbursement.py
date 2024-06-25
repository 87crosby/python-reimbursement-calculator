from datetime import datetime, timedelta

class Project:
    def __init__(self, city_type, start_date, end_date):
        self.city_type = city_type # 'high' or 'low' cost city
        self.start_date = datetime.strptime(start_date, "%m/%d/%y")
        self.end_date = datetime.strptime(end_date, "%m/%d/%y")



# Define the scenarios
set1 = [Project("low", "9/1/15", "9/3/15")]

set2 = [Project("low", "9/1/15", "9/1/15"),
        Project("high", "9/2/15", "9/6/15"),
        Project("low", "9/6/15", "9/8/15")]

set3 = [Project("low", "9/1/15", "9/3/15"),
        Project("high", "9/5/15", "9/7/15"),
        Project("high", "9/8/15", "9/8/15")]

set4 = [Project("low", "9/1/15", "9/1/15"),
        Project("low", "9/1/15", "9/1/15"),
        Project("high", "9/2/15", "9/2/15"),
        Project("high", "9/2/15", "9/3/15")]