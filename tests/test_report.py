import pytest
from src.models import EmployeePosition
from src.reports import PerformanceReport, get_report_generator

def test_performance_report_calculation(sample_developers):
    report = PerformanceReport()
    result = report.generate(sample_developers)

    assert len(result) == 2

    assert result[0]["position"] == "Backend"
    assert result[1]["position"] == "Frontend"

    assert result[0]["average_performance"] == 4.5
    assert result[1]["average_performance"] == 3.0

def test_unknown_report_raises_error():
    with pytest.raises(ValueError):
        get_report_generator("invalid_report_name")

def test_performance_report_headers():
    report = PerformanceReport()
    assert "Position" in report.headers
    assert "Average Performance" in report.headers


import tempfile
import os
from src.loader import load_data

def test_load_csv_data():
    csv_content = (
        "name,position,completed_tasks,performance,skills,team,experience_years\n"
        "Alex,Dev,10,5.0,\"Python\",A,1\n"
    )

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name

    try:
        data = load_data([tmp_path])
        assert len(data) == 1
        assert data[0].name == "Alex"
        assert data[0].performance == 5.0
        assert data[0].skills == ["Python"]
    finally:
        os.remove(tmp_path)