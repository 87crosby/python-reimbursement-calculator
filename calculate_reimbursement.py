from datetime import datetime, timedelta
from typing import List, Literal, Set

class Project:
    def __init__(self, city_type: Literal["high", "low"], start_date: str, end_date: str):
        self.city_type: Literal["high", "low"] = city_type # 'high' or 'low' cost city
        self.start_date: datetime = datetime.strptime(start_date, "%m/%d/%y")
        self.end_date: datetime = datetime.strptime(end_date, "%m/%d/%y")

def calculate_reimbursement(projects: List[Project]) -> int:
    # Sort projects by start date
    projects.sort(key=lambda x: x.start_date)
    
    # Collect all unique dates across all projects
    dates: Set[datetime] = set()
    for project in projects:
        current_date: datetime = project.start_date
        while current_date <= project.end_date:
            dates.add(current_date)
            current_date += timedelta(days=1)
    
    # Sort the unique dates
    dates_list: List[datetime] = sorted(list(dates))
    
    total_reimbursement: int = 0
    for i, date in enumerate(dates_list):
        # Determine if it's a travel day
        is_travel_day: bool = (i == 0 or i == len(dates_list) - 1 or 
                               (i > 0 and (date - dates_list[i-1]).days > 1))
        
        # Find the city type for the current date
        city_type: Literal["high", "low"] = next(
            (p.city_type for p in projects if p.start_date <= date <= p.end_date), 
            "low"
        )
        
        # Calculate rate based on travel day and city type
        if is_travel_day:
            rate: int = 55 if city_type == "high" else 45 # Travel day rates
        else:
            rate: int = 85 if city_type == "high" else 75 # Full day rates
        
        total_reimbursement += rate
    
    return total_reimbursement

def run_scenario(scenario: int, projects: List[Project]) -> None:
    print(f"Set {scenario}:")
    # Print details of each project in the scenario
    for i, project in enumerate(projects, 1):
        print(f"  Project {i}: {project.city_type.capitalize()} Cost City, "
              f"Start Date: {project.start_date.strftime('%m/%d/%y')}, "
              f"End Date: {project.end_date.strftime('%m/%d/%y')}")
    
    # Calculate and print the total reimbursement for the scenario
    reimbursement: int = calculate_reimbursement(projects)
    print(f"Total Reimbursement: ${reimbursement}\n")

# Define the scenarios
set1: List[Project] = [Project("low", "9/1/15", "9/3/15")]

set2: List[Project] = [
    Project("low", "9/1/15", "9/1/15"),
    Project("high", "9/2/15", "9/6/15"),
    Project("low", "9/6/15", "9/8/15")
]

set3: List[Project] = [
    Project("low", "9/1/15", "9/3/15"),
    Project("high", "9/5/15", "9/7/15"),
    Project("high", "9/8/15", "9/8/15")
]

set4: List[Project] = [
    Project("low", "9/1/15", "9/1/15"),
    Project("low", "9/1/15", "9/1/15"),
    Project("high", "9/2/15", "9/2/15"),
    Project("high", "9/2/15", "9/3/15")
]

# Run all scenarios
run_scenario(1, set1)
run_scenario(2, set2)
run_scenario(3, set3)
run_scenario(4, set4)