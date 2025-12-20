import csv
from pathlib import Path
from typing import List
from src.models import EmployeePosition

def load_data(file_paths: List[str]) -> List[EmployeePosition]:
    employee_positions = []

    for path in file_paths:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with file_path.open(mode='r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    employee_positions.append(EmployeePosition(
                        name=row['name'],
                        position=row['position'],
                        completed_tasks=int(row['completed_tasks']),
                        performance=float(row['performance']),
                        skills=[s.strip() for s in row['skills'].split(',')],
                        team=row['team'],
                        experience_years=int(row['experience_years'])
                    ))
                except (ValueError, KeyError) as e:
                    print(f"Skipping invalid row in {path}: {e}")
                    continue

    return employee_positions