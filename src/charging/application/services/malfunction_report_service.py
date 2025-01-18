from datetime import datetime
import pandas as pd
from src.charging.domain.search.entities.malfunction_report_entities import MalfunctionReport
from src.charging.domain.search.events.malfunction_report_events import MalfunctionReported
from src.charging.domain.search.value_objects.malfunction_report_value_objects import PostalCode, PhoneNumber, Email
from src.charging.infrastructure.repositories.malfunction_report_repository import MalfunctionReportRepository

class MalfunctionReportingService:
    def __init__(self, report_repository: MalfunctionReportRepository):
        self.report_repository = report_repository

    def report_malfunction(
        self, postal_code: str, station_id: str, user_name: str, user_email: str, user_phone_number: str, description: str
    ) -> MalfunctionReported:
        
        report = MalfunctionReport(
            postal_code=PostalCode(postal_code),
            station_id=station_id,
            user_name=user_name,
            user_email=Email(user_email),
            user_phone_number=PhoneNumber(user_phone_number),
            description=description,
            timestamp=datetime.now()
        )
        
        self.report_repository.save_report(report)
        
        return MalfunctionReported(event=report)

    def get_reports_by_postal_code(self, postal_code: str):
        """Retrieve all reports for a specific postal code."""
        reports_data = self.report_repository.find_by_postal_code(PostalCode(str(postal_code)))  # Ensure string conversion
        
        reports = []
        for report in reports_data:
            reports.append(MalfunctionReport(
                postal_code=str(report['postal_code']),  # Convert to string
                station_id=report['station_id'],
                user_name=report['user_name'],
                user_email=report['user_email'],
                user_phone_number=report['user_phone_number'],
                description=report['description'],
                timestamp=pd.to_datetime(report['timestamp']),
                resolved=bool(report['resolved'])
            ))
        return reports


    def get_all_reports(self):
        """Retrieve all malfunction reports."""
        return self.report_repository.get_all_reports()
