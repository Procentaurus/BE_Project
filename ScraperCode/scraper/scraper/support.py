import csv

def read_col_from_csv(path, col_name):

    data = []

    try:
        with open(path, mode='r', encoding='utf-8-sig') as file:    
            reader = csv.DictReader(file)
            for row in reader:
                if col_name in row:
                    data.append(row[col_name])
        
        return data

    except FileNotFoundError:
        print(f"The file at '{path}' does not exist.")