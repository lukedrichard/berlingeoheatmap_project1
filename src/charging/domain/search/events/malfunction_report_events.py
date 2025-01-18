from dataclasses import dataclass
from src.charging.domain.search.entities.malfunction_report_entities import MalfunctionReport

@dataclass
class MalfunctionReported:
    event: MalfunctionReport
