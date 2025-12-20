import pytest
from src.models import EmployeePosition
from src.reports import PerformanceReport, get_report_generator


@pytest.fixture
def sample_developers():
    return [
        EmployeePosition("A", "Backend", 10, 5.0, [], "Team A", 2),
        EmployeePosition("B", "Backend", 10, 4.0, [], "Team A", 2),
        EmployeePosition("C", "Frontend", 10, 3.0, [], "Team B", 2),
    ]