import pandas as pd
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
    layer_selection = st.radio("Select Layer", ("Report a Malfunction", "See All Reports", "Searh by Postal Code"))
    if(layer_selection == 'Report a Malfunction'):
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

    if (layer_selection == 'See All Reports'):
        repository = MalfunctionReportRepository()
        service = MalfunctionReportingService(repository)

        try:
            reports = service.get_all_reports()
            for report in reports:
                output = '\n'.join(f"{key}: {value}" for key,value in report.items())
                st.text(output)

        except ValueError as e:
            st.write(f"Error: {e}")

    if(layer_selection == 'Searh by Postal Code'):

        user_input = (st.text_input("Enter a Postal Code:"))
        if user_input:
            try:
                repository = MalfunctionReportRepository()
                service = MalfunctionReportingService(repository)
                reports = service.get_reports_by_postal_code(user_input)

                if(len(reports) == 0):
                    st.write('There are no malfunction reports for this postal code. Please try again.')
                else:
                    for report in reports:
                        st.text(report)

            except ValueError as e:
                st.write(f"Error: {e}")
                
    return
