# program that reads the employee_data.csv file and 
# prints out details of each employee

# nathan galindo
# johnny bhojwani
# mis 4322
# TTH 12:30

input_file_path = "/Users/nathangalindo/Documents/Programming/Academic/readandwritefiles/employee_data.csv"

# read input file
with open(input_file_path, "r") as input_file:
    # skip header
    input_file.readline()

    # loop over each line in file
    for line in input_file:
        columns = line.strip().split(",")

        employee_id = columns[0]
        employee_name = columns[1]
        employee_age = columns[2]
        employee_salary = columns[3]
        employee_hours_worked = columns[4]
        employee_productivity = columns[5]
        employee_teams = columns[6]
        employee_bonus = columns[7]


        print(f"{employee_name}'s Information:\n")
        print(f"{dict(
            id=employee_id,
            name=employee_name,
            age=employee_age,
            salary=employee_salary,
            hours_worked=employee_hours_worked,
            productivity=employee_productivity,
            teams=employee_teams,
            bonus=employee_bonus
        )}\n")
    
print("Process complete!\n")