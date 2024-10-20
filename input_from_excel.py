import pandas as pd
from receipt_data import ReceiptData
from confidential_information import ConfidentialInformation

class ExcelInputReader:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def read_data(self):
        # Read the Excel file
        try:
            df = pd.read_excel(self.excel_file_path, engine='openpyxl')
        except Exception as e:
            print(f"Failed to read Excel file: {e}")
            return None

        # Create a ReceiptData object from the Excel data
        receipt_data = ReceiptData(
            client_id=df['Client ID'][0],
            departure_location=df['Departure Location'][0],
            arrival_location=df['Arrival Location'][0],
            start_date=df['Start Date'][0],
            start_time=df['Start Time'][0],
            end_date=df['End Date'][0],
            end_time=df['End Time'][0],
            base_fare=df['Base Fare'][0],
            tariff_a=df['Tariff A'][0],
            tariff_a_time=df['Tariff A Time'][0],
            tariff_a_price=df['Tariff A Price'][0],
            tariff_a_distance=df['Tariff A Distance'][0],
            tariff_a_distance_price=df['Tariff A Distance Price'][0],
            tariff_c_time=df['Tariff C Time'][0],
            tariff_c_price=df['Tariff C Price'][0],
            tariff_c_distance=df['Tariff C Distance'][0],
            tariff_c_distance_price=df['Tariff C Distance Price'][0],
            total_price=df['Total Price'][0],
            total_ttc=df['Total TTC'][0],
            tva_rate=df['TVA Rate'][0],
            tva_amount=df['TVA Amount'][0],
            minimum_fare=df['Minimum Fare'][0],
            contestation_address_1=df['Contestation Address 1'][0],
            contestation_address_2=df['Contestation Address 2'][0],
            contestation_address_3=df['Contestation Address 3'][0],
            contestation_address_4=df['Contestation Address 4'][0]
        )

        return receipt_data
