# main.py
import os

from confidential_information import ConfidentialInformation
from input_from_excel import ExcelInputReader
from output_to_pdf import print_receipt_pdf

# Create an instance of ConfidentialInformation
confidential_info = ConfidentialInformation(
    driver_name='John Doe',
    immatricule='XYZ1234',
    stat_number='STAT5678'
)

# Get the directory where main.py is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the Excel file (absolute path)
excel_file_path = os.path.join(current_directory, 'receipt_data.xlsx')

# Create an instance of ExcelInputReader
reader = ExcelInputReader(excel_file_path)

# Read data from Excel
receipt_data = reader.read_data()

# Create the receipt PDF
print_receipt_pdf("taxi_receipt.pdf", receipt_data, confidential_info)
