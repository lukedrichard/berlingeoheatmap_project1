from src.charging.application.services.malfunction_report_service import MalfunctionReportingService
from src.charging.infrastructure.repositories.malfunction_report_repository import MalfunctionReportRepository

# def malfunction_report():
#     repository = MalfunctionReportRepository()
#     service = MalfunctionReportingService(repository)

#     try:
#         report_event = service.report_malfunction(
#             postal_code="12345",
#             station_id="STN001",
#             user_name="John Doe",
#             user_email="johndoe@example.com",
#             user_phone_number="+1234567890",
#             description="Machine not working"
#         )

#         print(f"Malfunction Reported: {report_event}")

#     except ValueError as e:
#         print(f"Error: {e}")

def get_all_malfunction_report():
    repository = MalfunctionReportRepository()
    service = MalfunctionReportingService(repository)

    try:
        reports = service.get_all_reports()

        print(f"Malfunctions Reported: {reports}")

    except ValueError as e:
        print(f"Error: {e}")

# def get_malfunction_report_postal_code():
#     repository = MalfunctionReportRepository()
#     service = MalfunctionReportingService(repository)

#     try:
#         # Get malfunction reports by postal code
#         reports = service.get_reports_by_postal_code(postal_code="12345")
        
#         print(f"Malfunction Reported by Postal Code 12345:")
#         for report in reports:
#             print(report)

#     except ValueError as e:
#         print(f"Error: {e}")
