import pandas as pd
from itertools import cycle
from datetime import datetime, timedelta

# Define your team members
tops_members = ["Prapaisri (Cassy)", "Nirin (Ae)", "Grisanapong (Pond)"]
cds_ssp_mkp_members = ["Wahritsahra (Satang)", "Chanwit (Ice)", "Thachalongkorn (Ford)", "Tharit (Nery)", "Tongta (Earn)", "Bundit (New)", "Chutimon (Pleng)"]

# Define the month details
start_date = datetime(2024, 4, 1)  # Start of April 2024
end_date = datetime(2024, 4, 30)   # End of April 2024
total_days = (end_date - start_date).days + 1

# Create a DataFrame for the schedule
schedule = pd.DataFrame({
    'Date': [start_date + timedelta(days=i) for i in range(total_days)],
    'Day': [(start_date + timedelta(days=i)).strftime('%A') for i in range(total_days)]
})

# Assign the shifts
def assign_shifts(schedule, tops_members, cds_ssp_mkp_members):
    # Create cycles for each team and shift
    cycles = {
        'Morning_TOPS': cycle(tops_members),
        'Morning_CDS/SSP/MKP': cycle(cds_ssp_mkp_members),
        'Afternoon_TOPS': cycle(tops_members),
        'Afternoon_CDS/SSP/MKP': cycle(cds_ssp_mkp_members),
        'On-Call': cycle(tops_members + cds_ssp_mkp_members)
    }

    # Initialize columns for the schedule
    for shift in cycles.keys():
        schedule[shift] = ''

    # Assign shifts based on day type
    for index, row in schedule.iterrows():
        day_type = 'Weekend' if row['Day'] in ['Saturday', 'Sunday'] else 'Weekday'
        for shift_type in ['Morning', 'Afternoon']:
            team_type = 'TOPS' if 'TOPS' in shift_type else 'CDS/SSP/MKP'
            member_count = 1 if day_type == 'Weekend' and shift_type == 'Morning' else 2
            schedule.at[index, f'{shift_type}_{team_type}'] = ', '.join(next(cycles[f'{shift_type}_{team_type}']) for _ in range(member_count))

    # Assign on-call shifts ensuring no overlapping with working shifts
    for index, row in schedule.iterrows():
        while True:
            potential_on_call = next(cycles['On-Call'])
            if potential_on_call not in row.values:
                schedule.at[index, 'On-Call'] = potential_on_call
                break

    return schedule

# Generate the schedule
final_schedule = assign_shifts(schedule, tops_members, cds_ssp_mkp_members)

# Display the schedule
print(final_schedule.head(10))  # Print the first 10 days as a sample

# If you want to save this schedule to a CSV file:
final_schedule.to_csv('april_2024_schedule.csv', index=False)
