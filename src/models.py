from dataclasses import dataclass

@dataclass(frozen=True)
class EmployeePosition:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: list[str]
    team: str
    experience_years: int