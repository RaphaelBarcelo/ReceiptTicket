from escpos.printer import Usb

# Set up the USB connection (adjust with your printer's vendor_id and product_id)
p = Usb(0x04b8, 0x0e15)  # Example values for Epson printers

def print_receipt_esc_pos(receipt_data):
    # Print the receipt header
    p.text("NOTE DE TAXI\n")
    p.text("- DUPLICATA -\n\n")

    # Print confidential info
    p.text(f"Mr {receipt_data.client_name}\n")
    p.text(f"Immatricule: {receipt_data.immatricule}\n")
    p.text(f"Stat. n°: {receipt_data.stat_number}\n")
    p.text(f"Client: {receipt_data.client_id}\n\n")

    # Print departure and arrival locations
    p.text(f"Lieu départ: {receipt_data.departure_location}\n")
    p.text(f"Lieu arrivée: {receipt_data.arrival_location}\n\n")

    # Print date and time
    p.text("Date-heure de la course\n")
    p.text(f"Début: {receipt_data.start_date}    {receipt_data.start_time}\n")
    p.text(f"Fin:     {receipt_data.end_date}    {receipt_data.end_time}\n\n")

    # Print tariff details
    p.text(f"Prise en charge: {receipt_data.base_fare}€\n")
    p.text(f"TARIF A: {receipt_data.tariff_a}€\n")
    p.text(f"Temps: {receipt_data.tariff_a_time}min    {receipt_data.tariff_a_price}€\n")
    p.text(f"Dist: {receipt_data.tariff_a_distance}kms    {receipt_data.tariff_a_distance_price}€\n")
    p.text(f"TARIF C:\n")
    p.text(f"Temps: {receipt_data.tariff_c_time}min    {receipt_data.tariff_c_price}€\n")
    p.text(f"Dist: {receipt_data.tariff_c_distance}kms    {receipt_data.tariff_c_distance_price}€\n\n")

    # Print total and tax information
    p.text(f"Prix de la course: {receipt_data.total_price}€\n")
    p.text(f"TOTAL TTC: {receipt_data.total_ttc}€\n")
    p.text(f"Dont TVA: {receipt_data.tva_rate}    {receipt_data.tva_amount}€\n\n")

    # Print footer
    p.text(f"Course minimum: {receipt_data.minimum_fare}€\n")
    p.text("En cas de contestation écrire à:\n")
    p.text(f"{receipt_data.contestation_address_1}\n")
    p.text(f"{receipt_data.contestation_address_2}\n")
    p.text(f"{receipt_data.contestation_address_3}\n")
    p.text(f"{receipt_data.contestation_address_4}\n")

    # Cut the paper (if supported by the printer)
    p.cut()