import os

def edit_csv_line(csv_file, num, new_data):
    temp_file = "temp.csv"  # Temporary file to store modified data

    with open(csv_file, 'r') as file:
        lines = file.readlines()  # Read all lines from the CSV file

    # Modify the desired line with the new data
    print(lines[num])
    print(lines[num-1])
    lines[num - 1] = ','.join(new_data) + '\n'

    with open(temp_file, 'w') as file:
        file.writelines(lines)  # Write all modified lines to the temporary file

    # Replace the original file with the modified file
    os.remove(csv_file)
    os.rename(temp_file, csv_file)

# Example usage:
csv_file = "StudyletLeaderboard.csv"
num = 1
new_data = ["John", "Doe", "30", "john.doe@example.com"]

edit_csv_line(csv_file, num, new_data)
