import streamlit as st
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

def create_reporting_interface():
    with st.form(key='user_form'):
        postal_code = st.text_input('Postal Code: ')
        station_id = st.text_input('Station ID: ')
        name = st.text_input('Your Name: ')
        email = st.text_input('email: ')
        phone_number = st.text_input('Phone Number: ')
        message = st.text_input('Message: ')

        submit_button = st.form_submit_button(label ='Submit')

    if submit_button:
        try:
            repository = MalfunctionReportRepository()
            service = MalfunctionReportingService(repository)
            service.report_malfunction(postal_code, station_id, name, email, phone_number, message)
            st.write('Thank you for your help!')
        except Exception as e:
            st.write('Report Unsuccessful')
            st.write(f'Backend Error: {e}')

    return
