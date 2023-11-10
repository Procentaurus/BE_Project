import csv

with open("C:\\PG\\sem_5\\BE\Project\\ScrapResults\\category_data.csv", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Category ID', 'Active', 'Name', 'Parent category', 'Root category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()

    counter = 1
    categories = ["warsztat rowerowy", "akcesoria", "części", "odzież rowerowa"]
    sub_categories = [
        ["stojaki serwisowe na rower", "narzędzia-rowerowe"],
        ["błotniki rowerowe", "bagażniki rowerowe"],
        ["grupy-osprzętu", "rowerowe napinacze łańcucha"],
        ["bielizna rowerowa", "bluzy rowerowe"]
    ]

    for i in range(len(categories)):
        for j in range(len(sub_categories[0])):
            writer.writerow({
                'Category ID': counter,
                'Active': 1,
                'Name': sub_categories[i][j],
                'Parent category': categories[i],
                'Root category': 0,
            })
            counter += 1

    for i in range(len(categories)):
        writer.writerow({
            'Category ID': counter,
            'Active': 1,
            'Name': categories[i],
            'Parent category': "Strona główna",
            'Root category': 1,
        })
        counter += 1
