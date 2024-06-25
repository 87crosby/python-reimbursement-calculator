from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum
from typing import List, Dict

class CityType(Enum):
    LOW_COST = "Low Cost City"
    HIGH_COST = "High Cost City"

@dataclass
class Project:
    city_type: CityType
    start_date: date
    end_date: date

class ReimbursementCalculator:
    def __init__(self):
        self.rates = {
            "travel": {CityType.LOW_COST: 45, CityType.HIGH_COST: 55},
            "full": {CityType.LOW_COST: 75, CityType.HIGH_COST: 85},
        }

    def calculate_reimbursement(self, projects: List[Project]) -> int:
        if not projects:
            return 0

        projects.sort(key=lambda p: p.start_date)
        day_types: Dict[date, str] = {}
        city_types: Dict[date, CityType] = {}

        # Initialize all project days
        for project in projects:
            current_date = project.start_date
            while current_date <= project.end_date:
                if current_date not in day_types:
                    day_types[current_date] = "full"
                    city_types[current_date] = project.city_type
                else:
                    # If the day exists, choose the higher cost city
                    city_types[current_date] = max(city_types[current_date], project.city_type, key=lambda x: self.rates["full"][x])
                current_date += timedelta(days=1)

        # Set first and last days of the entire period as travel days
        all_dates = sorted(day_types.keys())
        if all_dates:
            day_types[all_dates[0]] = "travel"
            day_types[all_dates[-1]] = "travel"

        # Check for gaps and set adjacent days as travel days
        for i in range(1, len(all_dates)):
            if (all_dates[i] - all_dates[i-1]).days > 1:
                day_types[all_dates[i-1]] = "travel"
                day_types[all_dates[i]] = "travel"

        total_reimbursement = 0
        for current_date, day_type in day_types.items():
            city_type = city_types[current_date]
            total_reimbursement += self.rates[day_type][city_type]

        return total_reimbursement

def parse_date(date_str: str) -> date:
    month, day, year = map(int, date_str.split('/'))
    return date(2000 + year, month, day)

def create_project(city_type: str, start_date: str, end_date: str) -> Project:
    return Project(
        CityType.HIGH_COST if "High" in city_type else CityType.LOW_COST,
        parse_date(start_date),
        parse_date(end_date)
    )

def main():
    calculator = ReimbursementCalculator()

    scenarios = [
        [
            create_project("Low Cost City", "9/1/15", "9/3/15")
        ],
        [
            create_project("Low Cost City", "9/1/15", "9/1/15"),
            create_project("High Cost City", "9/2/15", "9/6/15"),
            create_project("Low Cost City", "9/6/15", "9/8/15")
        ],
        [
            create_project("Low Cost City", "9/1/15", "9/3/15"),
            create_project("High Cost City", "9/5/15", "9/7/15"),
            create_project("High Cost City", "9/8/15", "9/8/15")
        ],
        [
            create_project("Low Cost City", "9/1/15", "9/1/15"),
            create_project("Low Cost City", "9/1/15", "9/1/15"),
            create_project("High Cost City", "9/2/15", "9/2/15"),
            create_project("High Cost City", "9/2/15", "9/3/15")
        ]
    ]

    for i, scenario in enumerate(scenarios, 1):
        reimbursement = calculator.calculate_reimbursement(scenario)
        print(f"Set {i} Reimbursement: ${reimbursement}")

if __name__ == "__main__":
    main()