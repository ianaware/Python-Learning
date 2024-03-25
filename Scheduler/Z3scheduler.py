from z3 import *
import csv

# Define the staff members and days
staff_members = ['Tanggwa', 'Yim', 'Benz']
days_of_april = [f'April_{day}' for day in range(1, 31)]  # April 1-30

# Define variables for working days
work_days = {staff: {day: Bool(f'{staff}_{day}') for day in days_of_april} for staff in staff_members}

# Initial shift configuration
s = Solver()

# Adding constraints based on initial shift configurations
for day in days_of_april:
    # Assign regular shifts based on initial configuration
    day_num = int(day.split('_')[1])  # Extract day number from string
    s.add(work_days['Tanggwa'][day] == (0 <= (day_num - 1) % 7 <= 3))  # Mon-Thu
    s.add(work_days['Yim'][day] == (4 <= (day_num - 1) % 7 or (day_num - 1) % 7 == 0))  # Fri-Mon
    s.add(work_days['Benz'][day] == (1 <= (day_num - 1) % 7 <= 4))  # Tue-Fri

# Check if a solution exists
if s.check() == sat:
    m = s.model()
    # Write the solution to a CSV file
    with open('schedule_April_2024.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Day'] + staff_members)
        for day in days_of_april:
            row = [day] + [m[work_days[staff][day]].sexpr() for staff in staff_members]
            writer.writerow(row)
    print("April 2024 schedule written to schedule_April_2024.csv")
else:
    print("No solution found for April 2024")
