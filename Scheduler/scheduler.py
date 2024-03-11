import csv
from datetime import datetime, timedelta
from itertools import cycle

# Define the team members and month details
tops_team = ["Prapaisri", "Nirin", "Grisanapong"]
cds_ssp_mkp_team = ["Wahritsahra", "Chanwit", "Thachalongkorn", "Tharit", "Tongta", "Bundit", "Chutimon"]
month_days_2024 = {
    'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
    'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31
}

# Initial global variables
total_days = 0  # Will be set based on the month chosen
start_date = None  # Will be set based on the month chosen
schedule = {}  # To store the final schedule
on_call_shifts_per_month = 4  # Maximum on-call shifts per staff member per month

# Functions to initialize and fill the schedule
def set_schedule_month_and_days(selected_month):
    global total_days, start_date
    if selected_month in month_days_2024:
        total_days = month_days_2024[selected_month]
        start_date = datetime(2024, list(month_days_2024).index(selected_month) + 1, 1)

def updated_initialize_schedule():
    """Initialize the schedule with empty slots including on-call shifts"""
    for day in range(total_days):
        current_date = start_date + timedelta(days=day)
        schedule[current_date] = {
            "weekday": current_date.weekday() < 5,  # Monday to Friday
            "morning": {"TOPs": [], "CDS/SSP/MKP": []},
            "afternoon": {"TOPs": [], "CDS/SSP/MKP": []},
            "on-call": []  # Added on-call shifts
        }

def updated_fill_shifts():
    """Fill the shifts according to the new rules provided"""
    tops_cycle_morning = cycle(tops_team)
    tops_cycle_afternoon = cycle(tops_team)
    cds_ssp_mkp_cycle_morning = cycle(cds_ssp_mkp_team)
    cds_ssp_mkp_cycle_afternoon = cycle(cds_ssp_mkp_team)
    on_call_cycle = cycle(tops_team + cds_ssp_mkp_team)

    on_call_tracker = {name: 0 for name in tops_team + cds_ssp_mkp_team}

    for date, shifts in schedule.items():
        # Assign on-call shifts
        while len(shifts['on-call']) < 1 and any(val < on_call_shifts_per_month for val in on_call_tracker.values()):
            candidate = next(on_call_cycle)
            if on_call_tracker[candidate] < on_call_shifts_per_month:
                shifts['on-call'].append(candidate)
                on_call_tracker[candidate] += 1

        if shifts['weekday']:
            # Weekday assignments
            shifts['morning']['TOPs'].append(next(tops_cycle_morning))
            for _ in range(2):
                shifts['morning']['CDS/SSP/MKP'].append(next(cds_ssp_mkp_cycle_morning))
            shifts['afternoon']['TOPs'].append(next(tops_cycle_afternoon))
            for _ in range(2):
                shifts['afternoon']['CDS/SSP/MKP'].append(next(cds_ssp_mkp_cycle_afternoon))
        else:
            # Weekend assignments
            shifts['morning']['TOPs'].append(next(tops_cycle_morning))
            shifts['morning']['CDS/SSP/MKP'].append(next(cds_ssp_mkp_cycle_morning))
            for _ in range(2):
                shifts['afternoon']['CDS/SSP/MKP'].append(next(cds_ssp_mkp_cycle_afternoon))

def export_to_csv():
    """Export the schedule to a CSV file"""
    # Specify your own path here
    file_path = "C:\\Users\\ian.w\\OneDrive - AWARE CORPORATION LIMITED\\GitHub\\Python\\Python-Learning\\Scheduler\\shift_schedule.csv"
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Shift", "Team", "Members", "On-Call"])
        for date, shifts in schedule.items():
            for shift in ['morning', 'afternoon']:
                for team in ['TOPs', 'CDS/SSP/MKP']:
                    writer.writerow([date.strftime('%Y-%m-%d'), shift, team, ', '.join(shifts[shift][team])])
            writer.writerow([date.strftime('%Y-%m-%d'), "on-call", "All", ', '.join(shifts['on-call'])])

# Set the schedule month, initialize and fill the schedule, then export to CSV
set_schedule_month_and_days('March')
updated_initialize_schedule()
updated_fill_shifts()
export_to_csv()
