import pytest
from src.charging.application.services.malfunction_report_service import MalfunctionReportingService
from src.charging.infrastructure.repositories.malfunction_report_repository import MalfunctionReportRepository
from src.charging.domain.search.entities.malfunction_report_entities import MalfunctionReport
from src.charging.domain.search.value_objects.malfunction_report_value_objects import PostalCode, Email, PhoneNumber

class MockMalfunctionReportRepository(MalfunctionReportRepository):
    """Mock repository to avoid actual file operations."""
    def __init__(self):
        self._reports = []

    def save_report(self, report: MalfunctionReport):
        self._reports.append(report)

    def find_by_postal_code(self, postal_code: PostalCode):
        return [r for r in self._reports if str(r.postal_code) == str(postal_code.value)]

    def get_all_reports(self):
        return self._reports


def test_report_malfunction_for_valid_data():
    """Test reporting a malfunction with valid data."""
    # Arrange
    service = MalfunctionReportingService(MockMalfunctionReportRepository())
    postal_code = "12345"
    station_id = "STN001"
    user_name = "John Doe"
    user_email = "johndoe@example.com"
    user_phone_number = "+1234567890"
    description = "Machine not working"

    # Act
    result = service.report_malfunction(postal_code, station_id, user_name, user_email, user_phone_number, description)

    # Assert
    assert isinstance(result.event, MalfunctionReport)
    assert str(result.event.postal_code) == postal_code
    assert result.event.station_id == station_id
    assert result.event.user_name == user_name
    assert str(result.event.user_email) == user_email
    assert str(result.event.user_phone_number) == user_phone_number
    assert result.event.description == description
    assert not result.event.resolved  # Default should be False


def test_cannot_report_malfunction_for_invalid_email():
    """Test that an invalid email format raises an error."""
    service = MalfunctionReportingService(MockMalfunctionReportRepository())

    with pytest.raises(ValueError, match="Invalid email format"):
        service.report_malfunction("12345", "STN001", "John Doe", "invalid-email", "+1234567890", "Machine not working")


def test_cannot_report_malfunction_for_invalid_phone_number():
    """Test that an invalid phone number format raises an error."""
    service = MalfunctionReportingService(MockMalfunctionReportRepository())

    with pytest.raises(ValueError, match="Invalid phone number format"):
        service.report_malfunction("12345", "STN001", "John Doe", "johndoe@example.com", "invalid-phone", "Machine not working")


def test_cannot_report_malfunction_without_description():
    """Test that a malfunction report cannot be submitted without a description."""
    service = MalfunctionReportingService(MockMalfunctionReportRepository())

    with pytest.raises(ValueError, match="Description cannot be empty"):
        service.report_malfunction("12345", "STN001", "John Doe", "johndoe@example.com", "+1234567890", "")


def test_get_reports_by_postal_code():
    """Test retrieving malfunction reports by postal code."""
    # Arrange
    repository = MockMalfunctionReportRepository()
    service = MalfunctionReportingService(repository)
    service.report_malfunction("12345", "STN001", "John Doe", "johndoe@example.com", "+1234567890", "Machine not working")

    # Act
    reports = service.get_reports_by_postal_code("12345")

    # Assert
    assert len(reports) == 1
    assert str(reports[0].postal_code) == "12345"


def test_get_all_reports():
    """Test retrieving all malfunction reports."""
    # Arrange
    repository = MockMalfunctionReportRepository()
    service = MalfunctionReportingService(repository)
    service.report_malfunction("12345", "STN001", "John Doe", "johndoe@example.com", "+1234567890", "Machine not working")
    service.report_malfunction("67890", "STN002", "Jane Doe", "janedoe@example.com", "+9876543210", "Charger issue")

    # Act
    reports = service.get_all_reports()

    # Assert
    assert len(reports) == 2
