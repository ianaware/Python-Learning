from ortools.sat.python import cp_model
import pandas as pd
import calendar

# Define constants
EMPLOYEES = ['Tanggwa', 'Yim', 'Benz']
MONTHS = ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DAYS_IN_MONTH = [30, 31, 30, 31, 31, 30, 31, 30, 31]  # April to December 2024
SHIFT_CONFIGS = [
    {'Tanggwa': 'NI1', 'Yim': 'NI2', 'Benz': 'NI3'},  # April
    {'Tanggwa': ['NI2', 'NI3'], 'Yim': ['NI1', 'NI3'], 'Benz': ['NI1', 'NI2']},  # May
    {'Tanggwa': ['NI3', 'NI2'], 'Yim': ['NI3', 'NI1'], 'Benz': ['NI2', 'NI1']},  # June
    {'Tanggwa': ['NI2', 'NI3'], 'Yim': ['NI1', 'NI3'], 'Benz': ['NI1', 'NI2']},  # July
    {'Tanggwa': ['NI3', 'NI2'], 'Yim': ['NI3', 'NI1'], 'Benz': ['NI2', 'NI1']},  # August
    {'Tanggwa': ['NI2', 'NI3'], 'Yim': ['NI1', 'NI3'], 'Benz': ['NI1', 'NI2']},  # September
    {'Tanggwa': ['NI3', 'NI2'], 'Yim': ['NI3', 'NI1'], 'Benz': ['NI2', 'NI1']},  # October
    {'Tanggwa': ['NI2', 'NI3'], 'Yim': ['NI1', 'NI3'], 'Benz': ['NI1', 'NI2']},  # November
    {'Tanggwa': ['NI3', 'NI2'], 'Yim': ['NI3', 'NI1'], 'Benz': ['NI2', 'NI1']}   # December
]
PUBLIC_HOLIDAYS = {
    'April': [6, 8, 12, 13, 14, 15, 16],
    'May': [1, 4, 6, 22],
    'June': [3],
    'July': [20, 22, 28, 29],
    'August': [12],
    'October': [13, 14, 23],
    'December': [5, 10, 31]
    # November has no public holidays
}
SHIFT_DAYS = {
    'NI1': [0, 1, 2, 3],  # Monday to Thursday
    'NI2': [4, 5, 6, 0],  # Friday to Monday
    'NI3': [1, 2, 3, 4]   # Tuesday to Friday
}

# Schedule generation function
def generate_schedule(month_index, shift_patterns, apply_holidays=False, public_holidays=[]):
    model = cp_model.CpModel()
    work_vars = {}

    # Variables
    for name in EMPLOYEES:
        for day in range(1, DAYS_IN_MONTH[month_index] + 1):
            work_vars[(name, day)] = model.NewBoolVar(f'{name}_{day}')

    # Regular shift constraints
    for day in range(1, DAYS_IN_MONTH[month_index] + 1):
        weekday = (calendar.monthrange(2024, month_index + 4)[1] + day - 1) % 7
        for name in EMPLOYEES:
            shifts = shift_patterns[name] if isinstance(shift_patterns[name], list) else [shift_patterns[name]]
            model.AddBoolOr([work_vars[(name, day)] for shift in shifts if weekday in SHIFT_DAYS[shift]]).OnlyEnforceIf(work_vars[(name, day)])
            model.AddBoolOr([work_vars[(name, day)].Not() for shift in shifts if weekday not in SHIFT_DAYS[shift]]).OnlyEnforceIf(work_vars[(name, day)].Not())

    # Solve the model without public holidays first
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        print(f"Standard schedule generated for {MONTHS[month_index]} 2024.")
    else:
        print(f"No standard solution found for {MONTHS[month_index]} 2024.")
        return {}

    # If the user wants to apply holidays, modify the model for public holidays
    solution = {}
    if apply_holidays:
        for day in public_holidays:
            model.Add(sum(work_vars[(name, day)] for name in EMPLOYEES) == 1)
        status = solver.Solve(model)
        if status != cp_model.FEASIBLE and status != cp_model.OPTIMAL:
            print(f"No solution with holidays found for {MONTHS[month_index]} 2024.")
            return {}

    # Collect solutions
    for name in EMPLOYEES:
        solution[name] = [solver.Value(work_vars[(name, day)]) for day in range(1, DAYS_IN_MONTH[month_index] + 1)]
    
    return solution

# Main script execution
all_schedules = {}
output_directory = r'C:\Users\ian.w\OneDrive - AWARE CORPORATION LIMITED\GitHub\Python\Python-Learning\Scheduler\\'
for index, month in enumerate(MONTHS):
    print(f"Generating schedule for {month} 2024...")
    shifts = SHIFT_CONFIGS[index]  # Get shift configurations for the month
    apply_holidays = input(f"Do you want to apply public holidays to the {month} 2024 schedule? (yes/no): ").lower() == 'yes'
    public_days = PUBLIC_HOLIDAYS.get(month, [])
    schedule = generate_schedule(index, shifts, apply_holidays, public_days)
    all_schedules[month] = schedule
    # Output to CSV
    if schedule:
        df = pd.DataFrame(schedule, index=range(1, DAYS_IN_MONTH[index] + 1))
        df.to_csv(f'{output_directory}schedule_{month}_2024.csv', index_label='Day')
        print(f"Schedule for {month} 2024 saved to {output_directory}.")

# Print completion message
print("All schedules generated and saved.")
