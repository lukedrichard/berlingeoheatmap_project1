import os
import pandas as pd
from src.charging.domain.search.entities.malfunction_report_entities import MalfunctionReport
from src.charging.domain.search.value_objects.malfunction_report_value_objects import PostalCode, Email, PhoneNumber

class MalfunctionReportRepository:
    def __init__(self, csv_path='src/charging/infrastructure/datasets/malfunction_reports.csv'):
        self.csv_path = csv_path
        self._ensure_csv_headers()
        self._reports = []
        self._load_from_csv()

    def _ensure_csv_headers(self):
        """Ensure the CSV file has headers if it doesn't exist or is empty."""
        if not os.path.exists(self.csv_path) or os.path.getsize(self.csv_path) == 0:
            df = pd.DataFrame(columns=[
                "postal_code", "station_id", "user_name", "user_email",
                "user_phone_number", "description", "timestamp", "resolved"
            ])
            df.to_csv(self.csv_path, index=False)
            print(f"✅ Created CSV file with headers: {self.csv_path}")

    def _load_from_csv(self):
        """Load existing reports from the CSV file into memory."""
        if not os.path.exists(self.csv_path) or os.path.getsize(self.csv_path) == 0:
            print(f"⚠️ CSV file '{self.csv_path}' is empty.")
            return  

        try:
            df = pd.read_csv(self.csv_path)
            if df.empty:
                print(f"⚠️ CSV file '{self.csv_path}' has no data.")
                return

            for _, row in df.iterrows():
                report = MalfunctionReport(
                    postal_code=PostalCode(str(row['postal_code'])),
                    station_id=row['station_id'],
                    user_name=row['user_name'],
                    user_email=Email(row['user_email']),
                    user_phone_number=PhoneNumber(row['user_phone_number']),
                    description=row['description'],
                    timestamp=pd.to_datetime(row['timestamp']),
                    resolved=bool(row['resolved'])
                )
                self._reports.append(report)

        except pd.errors.EmptyDataError:
            print(f"⚠️ CSV file '{self.csv_path}' is empty or corrupted.")
        except pd.errors.ParserError:
            print(f"❌ CSV file '{self.csv_path}' is incorrectly formatted.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    def save_report(self, report: MalfunctionReport):
        """Save a new malfunction report to the CSV file."""
        report_data = pd.DataFrame([{
            "postal_code": str(report.postal_code),
            "station_id": report.station_id,
            "user_name": report.user_name,
            "user_email": str(report.user_email),
            "user_phone_number": str(report.user_phone_number),
            "description": report.description,
            "timestamp": report.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "resolved": report.resolved
        }])

        # Append to the CSV file, ensuring headers exist
        report_data.to_csv(self.csv_path, index=False, mode='a', header=False)

    def find_by_postal_code(self, postal_code: PostalCode):
        """Retrieve reports by postal code."""
        if not os.path.exists(self.csv_path) or os.path.getsize(self.csv_path) == 0:
            return []

        df = pd.read_csv(self.csv_path, dtype={'postal_code': str})  # Force postal_code as string
        return df[df['postal_code'] == str(postal_code.value)].to_dict(orient='records')

    def get_all_reports(self):
        """Return all stored reports as a list of MalfunctionReport objects."""
        if not os.path.exists(self.csv_path) or os.path.getsize(self.csv_path) == 0:
            return []

        df = pd.read_csv(self.csv_path, dtype={'postal_code': str})  # Force postal_code as string

        return df.to_dict(orient='records')
