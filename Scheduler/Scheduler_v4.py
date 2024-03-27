import csv
import os
from collections import defaultdict
from datetime import datetime, timedelta

# Define the base path for output files
base_path = r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Scheduler'

# Define team and initial shift assignments
team_shifts = {
    'Ae': 'AS1', 'Pleng': 'AS2', 'Pond': 'AS3', 'Nery': 'AS4', 'Ford': 'AS5',
    'Satang': 'AS6', 'Cassy': 'AS7', 'Earn': 'AS8', 'Ice': 'AS9', 'New': 'AS10'
}

# Shift configurations
shift_configurations = {
    'AS1': {'work_days': ['Mon', 'Tue', 'Wed', 'Thu'], 'on_call': ['Sun'], 'time': 'MO'},
    'AS2': {'work_days': ['Tue', 'Wed', 'Thu', 'Fri'], 'on_call': ['Mon'], 'time': 'MO'},
    'AS3': {'work_days': ['Tue', 'Wed', 'Thu', 'Fri'], 'on_call': ['Sat'], 'time': 'MO'},
    'AS4': {'work_days': ['Mon', 'Fri', 'Sat', 'Sun'], 'on_call': ['Thu'], 'time': 'MO'},
    'AS5': {'work_days': ['Mon', 'Sat', 'Sun'], 'on_call': ['Tue', 'Wed'], 'time': 'MO'},
    'AS6': {'work_days': ['Mon', 'Tue', 'Wed', 'Thu'], 'on_call': ['Sun'], 'time': 'AF'},
    'AS7': {'work_days': ['Tue', 'Wed', 'Thu', 'Fri'], 'on_call': ['Mon'], 'time': 'AF'},
    'AS8': {'work_days': ['Tue', 'Wed', 'Thu', 'Fri'], 'on_call': ['Sat'], 'time': 'AF'},
    'AS9': {'work_days': ['Mon', 'Fri', 'Sat', 'Sun'], 'on_call': ['Thu'], 'time': 'AF'},
    'AS10': {'work_days': ['Mon', 'Sat', 'Sun'], 'on_call': ['Tue', 'Fri'], 'time': 'AF'}
}

# Shift rotation pattern
rotation_pattern = [
    'AS1', 'AS10', 'AS3', 'AS2', 'AS9', 'AS1',
    'AS3', 'AS6', 'AS5', 'AS4', 'AS7', 'AS2',
    'AS5', 'AS8', 'AS4', 'AS6', 'AS5', 'AS8',
    'AS7', 'AS2', 'AS9', 'AS8', 'AS4', 'AS7',
    'AS9', 'AS1', 'AS10', 'AS10', 'AS3', 'AS6'
]

# Public holidays
public_holidays = {
    'April': ['2024-04-08', '2024-04-12', '2024-04-15', '2024-04-16'],
    'May': ['2024-05-01', '2024-05-06', '2024-05-22'],
    'June': ['2024-06-03']
}

def weekday_to_str(weekday):
    return ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][weekday]

def generate_monthly_schedule(year, month, team_shifts, shift_configurations, holidays):
    days_in_month = (datetime(year, month, 28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    days_in_month = days_in_month.day
    schedule = defaultdict(lambda: {'MO': [], 'AF': []})
    for day in range(1, days_in_month + 1):
        date = datetime(year, month, day)
        weekday = weekday_to_str(date.weekday())
        for member, shift_code in team_shifts.items():
            shift = shift_configurations[shift_code]
            if weekday in shift['work_days']:
                schedule[date.strftime("%Y-%m-%d")][shift['time']].append(member)
            elif date.strftime("%Y-%m-%d") in shift['on_call']:
                schedule[date.strftime("%Y-%m-%d")][shift['time']].append(f"{member} (On-call)")
        if date.strftime("%Y-%m-%d") in holidays:
            schedule[date.strftime("%Y-%m-%d")]['MO'] = schedule[date.strftime("%Y-%m-%d")]['MO'][:2]  # Assuming order matters
            schedule[date.strftime("%Y-%m-%d")]['AF'] = schedule[date.strftime("%Y-%m-%d")]['AF'][:2]
    return schedule

def rotate_shifts(team_shifts, rotation_sequence):
    return {member: rotation_sequence[(rotation_sequence.index(shift) + 1) % len(rotation_sequence)] for member, shift in team_shifts.items()}

def write_schedule_to_csv(schedule, filename):
    full_path = os.path.join(base_path, filename)  # Create the full file path
    with open(full_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Day', 'Morning Shift', 'Afternoon Shift'])  # Add 'Day' to the header
        for date_str, shifts in sorted(schedule.items()):
            date = datetime.strptime(date_str, "%Y-%m-%d")  # Convert string back to a date
            day_name = date.strftime("%A")  # Get the full day name
            writer.writerow([date_str, day_name, ', '.join(shifts['MO']), ', '.join(shifts['AF'])])

# Main logic
for month, days, year in [('April', 30, 2024), ('May', 31, 2024), ('June', 30, 2024)]:
    schedule = generate_monthly_schedule(year, datetime.strptime(month, "%B").month, team_shifts, shift_configurations, public_holidays[month])
    filename = f"{month}_2024_schedule.csv"
    write_schedule_to_csv(schedule, filename)
    team_shifts = rotate_shifts(team_shifts, rotation_pattern)
