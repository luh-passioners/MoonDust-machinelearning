import csv
import random

# Define the headers for the CSV file
headers = ['Transaction id', 'amount', 'merchant id', 'sector in company', 'day in month']

# Generate random data for the CSV file


def generate_random_data(min, max):
    transaction_id = random.randint(1, 10000)  
    amount = f'${random.randint(50, 1000)}.00'
    merchant_id = random.choice(['amazon', 'testing', 'google cloud', 'aws'])
    sector = random.choice(['hardware', 'r&d', 'swe', 'marketing'])
    day_in_month = random.randint(1, 30)
    return [transaction_id, amount, merchant_id, sector, day_in_month]

# Number of entries to generate
num_entries = 1000

# Generate and write the data with some outliers

with open('../new_transaction_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the headers
    for _ in range(num_entries):
        data = generate_random_data()

        # Introduce outliers occasionally (adjust probability as needed)
        if random.random() < 0.05:  # 5% chance of an outlier
            # Outlier examples (modify these for your specific use case)
            data[1] = '$10000.00'  # High amount outlier
            data[2] = 'unkown'  # Unknown merchant outlier

        writer.writerow(data)
