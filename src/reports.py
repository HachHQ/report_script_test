from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any
from collections import defaultdict
from statistics import mean
from src.models import EmployeePosition

class BaseReport(ABC):
    """Базовый класс для всех отчетов."""

    @abstractmethod
    def generate(self, data: List[EmployeePosition]) -> List[Dict[str, Any]]:
        """Возвращает список словарей с обработанными данными."""
        pass

    @property
    @abstractmethod
    def headers(self) -> List[str]:
        """Заголовки колонок для таблицы."""
        pass

class PerformanceReport(BaseReport):
    """Отчет по эффективности позиций."""

    def generate(self, data: List[EmployeePosition]) -> List[Dict[str, Any]]:
        grouped = defaultdict(list)
        for dev in data:
            grouped[dev.position].append(dev.performance)

        result = []
        for position, perf_values in grouped.items():
            avg_perf = mean(perf_values)
            result.append({
                "position": position,
                "average_performance": round(avg_perf, 2)
            })

        result.sort(key=lambda x: x["average_performance"], reverse=True)
        return result

    @property
    def headers(self) -> List[str]:
        return ["Position", "Average Performance"]

REPORT_REGISTRY = {
    "performance": PerformanceReport(),
}

def get_report_generator(report_name: str) -> BaseReport:
    if report_name not in REPORT_REGISTRY:
        raise ValueError(f"Unknown report type: {report_name}. Available: {list(REPORT_REGISTRY.keys())}")
    return REPORT_REGISTRY[report_name]