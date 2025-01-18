from src.charging.application.services.malfunction_report_service import MalfunctionReportingService
from src.charging.infrastructure.repositories.malfunction_report_repository import MalfunctionReportRepository
from src.tests.charging import station_search

def test_report_malfunction():
    """Test reporting a malfunction."""
    repository = MalfunctionReportRepository()
    service = MalfunctionReportingService(repository)

    print("\n[TEST] Reporting a malfunction...")
    try:
        report = service.report_malfunction(
            postal_code="12345",
            station_id="STN001",
            user_name="John Doe",
            user_email="johndoe@example.com",
            user_phone_number="+1234567890",
            description="Machine not working"
        )
        print(f"✅ Malfunction reported successfully: {report.event}")
    except Exception as e:
        print(f"❌ Failed to report malfunction: {e}")


def test_get_all_malfunction_reports():
    """Test retrieving all malfunction reports."""
    repository = MalfunctionReportRepository()
    service = MalfunctionReportingService(repository)

    print("\n[TEST] Retrieving all malfunction reports...")
    try:
        reports = service.get_all_reports()
        print(f"✅ Retrieved {len(reports)} reports.")
    except Exception as e:
        print(f"❌ Failed to retrieve reports: {e}")


def test_get_reports_by_postal_code():
    """Test retrieving malfunction reports by postal code."""
    repository = MalfunctionReportRepository()
    service = MalfunctionReportingService(repository)

    print("\n[TEST] Retrieving reports by postal code 12345...")
    try:
        reports = service.get_reports_by_postal_code("12345")
        print(f"✅ Found {len(reports)} reports for postal code 12345.")
    except Exception as e:
        print(f"❌ Failed to retrieve reports by postal code: {e}")


def test_station_search_by_valid_postal_code():
    """Test searching stations using a valid postal code."""
    print("\n[TEST] Searching stations by valid postal code...")
    try:
        station_search.test_search_stations_by_valid_postal_code()
        print("✅ Station search by valid postal code passed.")
    except Exception as e:
        print(f"❌ Station search by valid postal code failed: {e}")


def test_invalid_berlin_postal_code():
    """Test searching stations with an invalid Berlin postal code."""
    print("\n[TEST] Testing invalid Berlin postal code...")
    try:
        station_search.test_invalid_berlin_postal_code()
        print("✅ Invalid Berlin postal code test passed.")
    except Exception as e:
        print(f"❌ Invalid Berlin postal code test failed: {e}")


def run_all_tests():
    """Run all tests."""
    print("\n--- Running All Tests ---")
    
    test_report_malfunction()
    test_get_all_malfunction_reports()
    test_get_reports_by_postal_code()
    test_station_search_by_valid_postal_code()
    test_invalid_berlin_postal_code()


if __name__ == "__main__":
    run_all_tests()
