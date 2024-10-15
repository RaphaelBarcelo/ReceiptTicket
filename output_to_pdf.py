# taxi_receipt.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def print_receipt_pdf(output_filename, receipt_data):
    # Set up the canvas
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    # Define the positions and the content of the receipt
    c.setFont("Helvetica", 10)
    margin_x = 50
    start_y = height - 50
    line_height = 14

    # Header
    c.drawString(margin_x, start_y, "NOTE DE TAXI")
    c.drawString(margin_x, start_y - line_height, "- DUPLICATA -")

    # Confidential information placeholders
    c.drawString(margin_x, start_y - 3 * line_height, f"Mr {receipt_data.client_name}")
    c.drawString(margin_x, start_y - 4 * line_height, f"Immatricule: {receipt_data.immatricule}")
    c.drawString(margin_x, start_y - 5 * line_height, f"Stat. n\u00b0: {receipt_data.stat_number}")
    c.drawString(margin_x, start_y - 6 * line_height, f"Client: {receipt_data.client_id}")

    # Lieu depart/arrivee
    c.drawString(margin_x, start_y - 8 * line_height, f"Lieu d\u00e9part: {receipt_data.departure_location}")
    c.drawString(margin_x, start_y - 9 * line_height, f"Lieu arriv\u00e9e: {receipt_data.arrival_location}")

    # Date and time
    c.drawString(margin_x, start_y - 11 * line_height, "Date-heure de la course")
    c.drawString(margin_x, start_y - 12 * line_height, f"D\u00e9but: {receipt_data.start_date}    {receipt_data.start_time}")
    c.drawString(margin_x, start_y - 13 * line_height, f"Fin:     {receipt_data.end_date}    {receipt_data.end_time}")
    c.drawString(margin_x, start_y - 14 * line_height, "- DUPLICATA -")

    # Tariff details
    c.drawString(margin_x, start_y - 16 * line_height, f"Prise en charge:       {receipt_data.base_fare}\u20ac")
    c.drawString(margin_x, start_y - 17 * line_height, f"TARIF A         {receipt_data.tariff_a}\u20ac")
    c.drawString(margin_x, start_y - 18 * line_height, f"Temps:   {receipt_data.tariff_a_time}min     {receipt_data.tariff_a_price}\u20ac")
    c.drawString(margin_x, start_y - 19 * line_height, f"Dist:       {receipt_data.tariff_a_distance}kms       {receipt_data.tariff_a_distance_price}\u20ac")
    c.drawString(margin_x, start_y - 20 * line_height, "TARIF C")
    c.drawString(margin_x, start_y - 21 * line_height, f"Temps:     {receipt_data.tariff_c_time}min      {receipt_data.tariff_c_price}\u20ac")
    c.drawString(margin_x, start_y - 22 * line_height, f"Dist:       {receipt_data.tariff_c_distance}kms     {receipt_data.tariff_c_distance_price}\u20ac")

    # Total
    c.drawString(margin_x, start_y - 24 * line_height, f"Prix de la course:     {receipt_data.total_price}\u20ac")
    c.drawString(margin_x, start_y - 25 * line_height, f"TOTAL TTC:            {receipt_data.total_ttc}\u20ac")
    c.drawString(margin_x, start_y - 26 * line_height, f"Dont TVA: {receipt_data.tva_rate}     {receipt_data.tva_amount}\u20ac")

    # Footer
    c.drawString(margin_x, start_y - 28 * line_height, f"Quel que soit le montant, supplements inclus, la course minimum est de {receipt_data.minimum_fare}\u20ac")
    c.drawString(margin_x, start_y - 30 * line_height, "En cas de contestation \u00e9crire \u00e0:")
    c.drawString(margin_x, start_y - 31 * line_height, receipt_data.contestation_address_1)
    c.drawString(margin_x, start_y - 32 * line_height, receipt_data.contestation_address_2)
    c.drawString(margin_x, start_y - 33 * line_height, receipt_data.contestation_address_3)
    c.drawString(margin_x, start_y - 34 * line_height, receipt_data.contestation_address_4)

    # Save the PDF
    c.save()
