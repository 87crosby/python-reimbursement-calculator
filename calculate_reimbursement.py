from datetime import datetime, timedelta

class Project:
    def __init__(self, city_type, start_date, end_date):
        self.city_type = city_type
        self.start_date = datetime.strptime(start_date, "%m/%d/%y")
        self.end_date = datetime.strptime(end_date, "%m/%d/%y")