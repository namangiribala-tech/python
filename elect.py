def electbill(total_bill, usage_per_floor, total_usage):
    price_per_unit = total_bill / total_usage
    bill_per_floor = []
    for usage in usage_per_floor:
        bill = usage * price_per_unit
        bill_per_floor.append(bill)
    return bill_per_floor

# Input total electric bill
total_bill = float(input('Enter the total electric bill: '))

# Input number of floors
num_floors = int(input('Number of floors: '))

# Lists to store present and old readings
present_readings = []
old_readings = []

# Input present readings
for i in range(num_floors):
    present_reading = int(input(f'Enter present reading of floor {i+1}: '))
    present_readings.append(present_reading)

# Input old readings
for i in range(num_floors):
    old_reading = int(input(f'Enter old reading of floor {i+1}: '))
    old_readings.append(old_reading)

# Calculate usage per floor and total usage
usage_per_floor = []
total_usage = 0
for i in range(num_floors):
    usage = present_readings[i] - old_readings[i]
    usage_per_floor.append(usage)
    total_usage += usage

# Calculate and print the bill per floor
bills = electbill(total_bill, usage_per_floor, total_usage)
print('Electricity bill per floor:', bills)