from z3 import *
import csv

# Define the staff members
staff_members = ['Tanggwa', 'Yim', 'Benz']

# Define public holidays for each month
public_holidays = {
    'May': ['May_1', 'May_4', 'May_22'],
    'June': ['June_3'],
    'July': ['July_20'],
    'August': ['August_12'],
    'October': ['October_13', 'October_23'],
    'December': ['December_5', 'December_10']
}

# Function to create and save a monthly schedule
def create_monthly_schedule(year, month, days_in_month, shift_patterns, public_holidays):
    days_of_month = [f'{month}_{day}' for day in range(1, days_in_month + 1)]
    work_days = {staff: {day: Bool(f'{staff}_{day}') for day in days_of_month} for staff in staff_members}
    s = Solver()

    # Add constraints based on shift configurations
    for day in days_of_month:
        day_num = int(day.split('_')[1])
        for staff in staff_members:
            if shift_patterns[staff] == 'NI1':
                s.add(work_days[staff][day] == (0 <= (day_num - 1) % 7 <= 3))
            elif shift_patterns[staff] == 'NI2':
                s.add(work_days[staff][day] == (4 <= (day_num - 1) % 7 or (day_num - 1) % 7 == 0))
            elif shift_patterns[staff] == 'NI3':
                s.add(work_days[staff][day] == (1 <= (day_num - 1) % 7 <= 4))

    # Check and write the schedule
    if s.check() == sat:
        m = s.model()
        file_path = fr'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Scheduler\{year}_{month}_schedule.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Day'] + [f'{staff} ({shift_patterns[staff]})' for staff in staff_members])
            for day in days_of_month:
                row = [(f"{day} (PH)" if day in public_holidays.get(month, []) else day)] + \
                      [('WORKING' if m[work_days[staff][day]] else 'OFF') for staff in staff_members]
                writer.writerow(row)
        print(f"Schedule for {month} {year} written to {file_path}")
    else:
        print(f"No solution found for {month} {year}")

# Shift rotation sequence
rotation_sequence = [
    ('2024', 'April', 30, {'Tanggwa': 'NI1', 'Yim': 'NI2', 'Benz': 'NI3'}),
    ('2024', 'May', 31, {'Tanggwa': 'NI2', 'Yim': 'NI3', 'Benz': 'NI1'}),
    ('2024', 'June', 30, {'Tanggwa': 'NI3', 'Yim': 'NI1', 'Benz': 'NI2'}),
    ('2024', 'July', 31, {'Tanggwa': 'NI1', 'Yim': 'NI2', 'Benz': 'NI3'}),
    ('2024', 'August', 31, {'Tanggwa': 'NI2', 'Yim': 'NI3', 'Benz': 'NI1'}),
    ('2024', 'September', 30, {'Tanggwa': 'NI3', 'Yim': 'NI1', 'Benz': 'NI2'}),
    ('2024', 'October', 31, {'Tanggwa': 'NI1', 'Yim': 'NI2', 'Benz': 'NI3'}),
    ('2024', 'November', 30, {'Tanggwa': 'NI2', 'Yim': 'NI3', 'Benz': 'NI1'}),
    ('2024', 'December', 31, {'Tanggwa': 'NI3', 'Yim': 'NI1', 'Benz': 'NI2'})
]

# Generate and save the schedules for each month
for year, month, days_in_month, shift_patterns in rotation_sequence:
    create_monthly_schedule(year, month, days_in_month, shift_patterns, public_holidays)
