# main.py
from output_to_pdf import print_receipt_pdf
from receipt_data import ReceiptData

# Create an instance of ReceiptData with the required values
receipt_data = ReceiptData(
    client_name='John Doe',
    immatricule='XYZ1234',
    stat_number='STAT5678',
    client_id='CLIENT91011',
    departure_location='123 Main St',
    arrival_location='456 Elm St',
    start_date='12-10-2024',
    start_time='15h56',
    end_date='12-10-2024',
    end_time='16h56',
    base_fare='2.12',
    tariff_a='17.00',
    tariff_a_time='24.27',
    tariff_a_price='9.40',
    tariff_a_distance='6.6',
    tariff_a_distance_price='7.40',
    tariff_c_time='2.49',
    tariff_c_price='1.00',
    tariff_c_distance='19.0',
    tariff_c_distance_price='43.20',
    total_price='63.32',
    total_ttc='63.32',
    tva_rate='10.00%',
    tva_amount='5.76',
    minimum_fare='7.30',
    contestation_address_1="DDPP de l'AISNE",
    contestation_address_2='ESPACE SYMBIOSE',
    contestation_address_3='80 rue Pierre-Gilles de Gennes',
    contestation_address_4='02000 BARENTON BUGNY'
)

# Create the receipt PDF
print_receipt_pdf("taxi_receipt.pdf", receipt_data)
