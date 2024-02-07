# program that reads the file customers.csv and produces a new 
# file containing the customer name and country they are from

# nathan galindo
# johnny bhojwani
# mis 4322
# TTH 12:30

input_file_path = '/Users/nathangalindo/Documents/Programming/Academic/readandwritefiles/customers.csv' # origin file containing customer info
output_file_path = './readandwritefiles/customer_country.csv' # file this program creates

# use `open` function to read 'r' from `input_file`
# use `open` function to write 'w' to `output_file`
with open(input_file_path, 'r') as input_file, open (output_file_path, 'w') as output_file:
    header = input_file.readline()

    output_file.write(f"FirstName,LastName,Country\n")

    for line in input_file:
        columns = line.strip().split(",")

        first_name = columns[1]
        last_name = columns[2]
        country = columns[4]

        output_file.write(f"{first_name},{last_name},{country}\n")

print("Process complete!")