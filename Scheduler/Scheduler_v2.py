from ortools.sat.python import cp_model

def main():
    # Define data for scheduling
    num_days = 7  # For one week
    num_weeks = 4  # Assume a four-week schedule for spreading on-call shifts
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    shifts = ['Morning', 'Afternoon', 'On-call']
    employees = ['Cassy', 'Ae', 'Pond', 'Satang', 'Ice', 'Ford', 'Nery', 'Earn', 'New', 'Pleng']
    shift_requirements = {
        'Weekdays': {'Morning': 3, 'Afternoon': 3},
        'Weekend': {'Morning': 2, 'Afternoon': 2}
    }
    # Weekday and weekend identification
    weekdays = days[:5]
    weekend = days[5:]

    # Model creation
    model = cp_model.CpModel()

    # Create variables
    schedules = {}
    for employee in employees:
        for week in range(num_weeks):
            for day in days:
                for shift in shifts:
                    schedules[(employee, week, day, shift)] = model.NewBoolVar(f'{employee}_{week}_{day}_{shift}')

    # Constraints
    # Staffing requirements
    for week in range(num_weeks):
        for day in days:
            day_type = 'Weekend' if day in weekend else 'Weekdays'
            for shift in ['Morning', 'Afternoon']:
                model.Add(sum(schedules[(employee, week, day, shift)] for employee in employees) == shift_requirements[day_type][shift])

    # Shift exclusivity and regular work requirements
    for employee in employees:
        for week in range(num_weeks):
            # Exclusive shift type per month
            model.Add(sum(schedules[(employee, week, day, 'Morning')] for day in days) <= 5)  # Assuming month exclusive but week bounded
            model.Add(sum(schedules[(employee, week, day, 'Afternoon')] for day in days) <= 5)
            # On-call shifts separate from regular shifts
            for day in days:
                model.Add(schedules[(employee, week, day, 'On-call')] + schedules[(employee, week, day, 'Morning')] <= 1)
                model.Add(schedules[(employee, week, day, 'On-call')] + schedules[(employee, week, day, 'Afternoon')] <= 1)
            # Each staff member must work four regular shifts and one on-call shift per week
            model.Add(sum(schedules[(employee, week, day, shift)] for day in days for shift in ['Morning', 'Afternoon']) == 4)
            model.Add(sum(schedules[(employee, week, day, 'On-call')] for day in days) == 1)
            # Consecutive days off
            for first_day_off in range(5):  # Starting index for two consecutive days off
                model.Add(sum(schedules[(employee, week, day, shift)] for day in days[first_day_off:first_day_off+2] for shift in shifts) >= 1)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Output the results
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for week in range(num_weeks):
            print(f"Week {week+1}:")
            for day in days:
                print(f"  {day}:")
                for shift in shifts:
                    working_employees = [employee for employee in employees if solver.Value(schedules[(employee, week, day, shift)])]
                    print(f"    {shift}: {', '.join(working_employees)}")
            print()
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()