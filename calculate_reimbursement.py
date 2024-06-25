from datetime import datetime, timedelta

class Project:
    def __init__(self, city_type, start_date, end_date):
        self.city_type = city_type # 'high' or 'low' cost city
        self.start_date = datetime.strptime(start_date, "%m/%d/%y")
        self.end_date = datetime.strptime(end_date, "%m/%d/%y")

def calculate_reimbursement(projects):
    # Sort projects by start date
    projects.sort(key=lambda x: x.start_date)
    
    # Collect all unique dates across all projects
    dates = set()
    for project in projects:
        current_date = project.start_date
        while current_date <= project.end_date:
            dates.add(current_date)
            current_date += timedelta(days=1)
    
    # Sort the unique dates
    dates = sorted(list(dates))
    
    total_reimbursement = 0
    for i, date in enumerate(dates):
        # Determine if it's a travel day
        is_travel_day = (i == 0 or i == len(dates) - 1 or 
                        (i > 0 and (date - dates[i-1]).days > 1))
        
        # Find the city type for the current date
        city_type = next((p.city_type for p in projects if p.start_date <= date <= p.end_date), "low")
        
        # Calculate rate based on travel day and city type
        if is_travel_day:
            rate = 55 if city_type == "high" else 45  # Travel day rates
        else:
            rate = 85 if city_type == "high" else 75  # Full day rates
        
        total_reimbursement += rate
    
    return total_reimbursement



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

print(calculate_reimbursement(set1))
print(calculate_reimbursement(set2))
print(calculate_reimbursement(set3))
print(calculate_reimbursement(set4))