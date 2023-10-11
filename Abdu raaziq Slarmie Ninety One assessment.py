def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            object = line.strip().split(',')
            data.append({'First Name': object[0], 'Last Name': object[1], 'Marks': int(object[2])})
    return data

def display_sorted_marks(data):
    sorted_data = sorted(data, key=lambda x: x['Marks'], reverse = True)
    for object in sorted_data:
        print(f"{object['First Name']} {object['Last Name']} --- {object['Marks']}")

def main():
    file_path = 'TestData.csv' 
    data = read_csv(file_path)

    if not data:
        print("No data found in the CSV file.")
    else:
        display_sorted_marks(data)

if __name__ == '__main__':
    main()
