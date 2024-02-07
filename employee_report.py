# Use employee_data.csv. Management would like to know which 
# of their employees are highly efficient and which are not. 
# Efficiency can be calculated by dividing the productivity by 
# hours worked. An employee is considered highly efficient if 
# the efficiency factor is greater than 2. An employee is considered 
# inefficient if the efficiency factor is below 1. Management would 
# also like to know who and how many are in different age 
# categories - 20s, 30s and 40s. Reproduce the report as show 
# below (print statements).

# efficiency factor = productivity / hours worked

# highly efficient -> efficiency factor > 2
# inefficient -> efficiency factor < 1

# nathan galindo
# johnny bhojwani
# mis 4322
# TTH 12:30

input_file_path = "/Users/nathangalindo/Documents/Programming/Academic/readandwritefiles/employee_data.csv"

with open(input_file_path, "r") as input_file:
    # skip header
    input_file.readline()

    # initialize employee groupings
    highly_efficient_employees = []
    inefficient_employees = []
    employees_in_forties = []
    employees_in_thirties = []
    employees_in_twenties = []

    for line in input_file:
        # remove whitespace; split string into list of substrings
        columns = line.strip().split(",")

        name = columns[1]
        age = float(columns[2])
        productivity = float(columns[5])
        hours_worked = float(columns[4])

        # determine employee efficiency
        efficiency_factor = productivity / hours_worked
        if efficiency_factor > 2:
            highly_efficient_employees.insert(0, name)
        elif efficiency_factor < 1:
            inefficient_employees.insert(0, name)

        # group employees by age
        if age >= 40 and age < 50:
            employees_in_forties.insert(0, name)
        elif age >= 30 and age < 40:
            employees_in_thirties.insert(0, name)
        elif age >= 20 and age < 30:
            employees_in_twenties.insert(0, name)
        
        print("Highly Efficient Individuals:\n")
        for employee in highly_efficient_employees:
            print(employee)
        
        print()

        print("Low Efficiency Individuals:\n")
        for employee in inefficient_employees:
            print(employee)
        
        print()

        print("Employees in their 40s:\n")
        for employee in employees_in_forties:
            print(employee)

        print(f"\nTotal number of employees in their 40s: {len(employees_in_forties)}\n")

        print("Employees in their 30s:\n")
        for employee in employees_in_thirties:
            print(employee)

        print(f"\nTotal number of employees in their 30s: {len(employees_in_thirties)}\n")

        print("Employees in their 20s:\n")
        for employee in employees_in_twenties:
            print(employee)

        print(f"\nTotal number of employees in their 20s: {len(employees_in_twenties)}\n")
