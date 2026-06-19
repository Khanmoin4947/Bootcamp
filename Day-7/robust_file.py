import csv

try:
    file = open("data.csv")
    reader = csv.reader(file)
    total = 0
    count = 0
    for row in reader:
        total += float(row[0])
        count += 1
    print("Average =", total / count)

except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except csv.Error:
    print("CSV Error!")
finally:
    file.close()
    print("File closed")