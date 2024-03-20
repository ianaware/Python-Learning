import pandas as pd
from ortools.sat.python import cp_model

def create_shift_schedule():
    # Define the data for scheduling
    employees = ['Tanggwa', 'Benz', 'Yim']
    months = ['April', 'May', 'June']
    month_days = {'April': 30, 'May': 31, 'June': 30}  # Days in each month
    
    # Corrected rotation for the shift patterns for each month
    shift_off_days = {
        'April': {'Tanggwa': ['Friday', 'Saturday', 'Sunday'], 'Benz': ['Saturday', 'Sunday', 'Monday'], 'Yim': ['Tuesday', 'Wednesday', 'Thursday']},
        'May': {'Benz': ['Friday', 'Saturday', 'Sunday'], 'Tanggwa': ['Tuesday', 'Wednesday', 'Thursday'], 'Yim': ['Saturday', 'Sunday', 'Monday']},
        'June': {'Tanggwa': ['Saturday', 'Sunday', 'Monday'], 'Benz': ['Tuesday', 'Wednesday', 'Thursday'], 'Yim': ['Friday', 'Saturday', 'Sunday']}
    }
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Base directory
    base_directory = r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Scheduler\\'

    for month in months:
        # Initialize model inside loop to reset constraints for each month
        model = cp_model.CpModel()

        # List to collect all schedule data
        schedules_data = []  

        # Create schedules data
        for day in range(1, month_days[month] + 1):
            day_name = day_names[(day - 1) % 7]
            day_schedule = {'Day': f'{day_name} {day}'}
            for employee in employees:
                # Create the variable for each employee's schedule
                var = model.NewBoolVar(f'{employee}_{month}_{day}')
                # Check if the employee is supposed to work this day
                model.Add(var == 1).OnlyEnforceIf(model.NewBoolVar(f'working_{employee}_{month}_{day}'))
                model.Add(var == 0).OnlyEnforceIf(model.NewBoolVar(f'off_{employee}_{month}_{day}'))
                day_schedule[employee] = 'Work' if day_name not in shift_off_days[month][employee] else 'Off'
            schedules_data.append(day_schedule)
        
        # Convert schedules data to DataFrame
        df = pd.DataFrame(schedules_data)

        # Create a DataFrame for the shift pattern
        shift_pattern_df = pd.DataFrame({
            'Employee': list(shift_off_days[month].keys()),
            'Shift Pattern': [', '.join(days) + ' off' for days in shift_off_days[month].values()]
        })

        # Save the DataFrame to an Excel file for the current month
        output_filepath = base_directory + f'{month}_schedule.xlsx'
        with pd.ExcelWriter(output_filepath, engine='openpyxl') as writer:
            shift_pattern_df.to_excel(writer, sheet_name='Shift Patterns', index=False)
            df.to_excel(writer, sheet_name='Schedule', index=False)
        print(f'Schedule for {month} saved to {output_filepath}')

if __name__ == '__main__':
    create_shift_schedule()
