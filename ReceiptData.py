# receipt_data.py

class ReceiptData:
    def __init__(
        self,
        client_name,
        immatricule,
        stat_number,
        client_id,
        departure_location,
        arrival_location,
        start_date,
        start_time,
        end_date,
        end_time,
        base_fare,
        tariff_a,
        tariff_a_time,
        tariff_a_price,
        tariff_a_distance,
        tariff_a_distance_price,
        tariff_c_time,
        tariff_c_price,
        tariff_c_distance,
        tariff_c_distance_price,
        total_price,
        total_ttc,
        tva_rate,
        tva_amount,
        minimum_fare,
        contestation_address_1,
        contestation_address_2,
        contestation_address_3,
        contestation_address_4
    ):
        self.client_name = client_name
        self.immatricule = immatricule
        self.stat_number = stat_number
        self.client_id = client_id
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.base_fare = base_fare
        self.tariff_a = tariff_a
        self.tariff_a_time = tariff_a_time
        self.tariff_a_price = tariff_a_price
        self.tariff_a_distance = tariff_a_distance
        self.tariff_a_distance_price = tariff_a_distance_price
        self.tariff_c_time = tariff_c_time
        self.tariff_c_price = tariff_c_price
        self.tariff_c_distance = tariff_c_distance
        self.tariff_c_distance_price = tariff_c_distance_price
        self.total_price = total_price
        self.total_ttc = total_ttc
        self.tva_rate = tva_rate
        self.tva_amount = tva_amount
        self.minimum_fare = minimum_fare
        self.contestation_address_1 = contestation_address_1
        self.contestation_address_2 = contestation_address_2
        self.contestation_address_3 = contestation_address_3
        self.contestation_address_4 = contestation_address_4
